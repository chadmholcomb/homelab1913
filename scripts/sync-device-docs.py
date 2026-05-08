#!/usr/bin/env python3
"""
sync-device-docs.py

Reads docs/network.json (NetJSON NetworkGraph) and updates each device's
markdown file:
  - H1 title line        →  # TAG — Label
  - <!-- NETJSON:START/END -->              device info table
  - <!-- NETJSON:INTERFACES:START/END -->   interface/port table

Also updates README.md device registry (grouped by subsystem, sorted by tag).

Edit docs/network.json to update device info, then run this script to
propagate those changes to all device documentation files.

Usage:
    python3 scripts/sync-device-docs.py              # sync all docs
    python3 scripts/sync-device-docs.py --dry-run    # preview changes, no writes
    python3 scripts/sync-device-docs.py --validate   # check for inconsistencies only
    python3 scripts/sync-device-docs.py --validate --dry-run  # both
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NETWORK_JSON = REPO_ROOT / "docs" / "network.json"

SUBSYSTEM_LABELS = {
    "development": "Development Subsystem",
    "ema": "Energy Management Assembly",
    "target": "Target Hardware",
}

SUBSYSTEM_ORDER = ["development", "ema", "target"]

# Pattern matching tag-like tokens (e.g. MOD-1, NS-2, RTAC-1)
TAG_PATTERN = re.compile(r'\b([A-Z]{2,6}-\d+)\b')

# Interface/protocol technology names that match the tag pattern but are not tags
KNOWN_NON_TAGS = {"RS-232", "RS-485", "RS-422", "RS-423", "RS-449",
                  "HDMI-1", "HDMI-2", "DP-1", "DP-2", "EDP-1", "eDP-1"}

# Pattern to extract IPs from strings (e.g. management_url)
_IP_PAT = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b')


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def render_info_block(node: dict) -> str:
    p = node.get("properties", {})
    addresses = node.get("local_addresses", [])
    rows = [
        ("Tag",            node["id"]),
        ("Manufacturer",   p.get("manufacturer") or "TBD"),
        ("Model",          p.get("model") or "TBD"),
        ("Type",           p.get("type") or "TBD"),
        ("Subsystem",      SUBSYSTEM_LABELS.get(p.get("subsystem", ""), p.get("subsystem") or "TBD")),
        ("Hostname",       p.get("hostname") or "TBD"),
        ("IP Address",     ", ".join(addresses) if addresses else "TBD"),
        ("MAC Address",    p.get("mac_address") or "TBD"),
        ("Serial Number",  p.get("serial_number") or "TBD"),
        ("Management",     p.get("management_platform") or "TBD"),
        ("Management URL", p.get("management_url") or "TBD"),
    ]
    lines = [
        "<!-- NETJSON:START -->",
        "| Field | Value |",
        "|-------|-------|",
    ]
    for field, value in rows:
        lines.append(f"| **{field}** | {value} |")
    lines.append("<!-- NETJSON:END -->")
    return "\n".join(lines)


def render_interfaces_block(node: dict) -> str:
    interfaces = node.get("properties", {}).get("interfaces", [])
    lines = [
        "<!-- NETJSON:INTERFACES:START -->",
        "| Interface | Type | Role | Address | Notes |",
        "|-----------|------|------|---------|-------|",
    ]
    if interfaces:
        for iface in interfaces:
            addrs = ", ".join(iface.get("addresses", [])) or "TBD"
            notes = iface.get("notes", "")
            lines.append(
                f"| {iface['name']} | {iface['type']} | {iface.get('role', 'TBD')} | {addrs} | {notes} |"
            )
    else:
        lines.append("| — | TBD | TBD | TBD | |")
    lines.append("<!-- NETJSON:INTERFACES:END -->")
    return "\n".join(lines)


def render_registry_block(nodes: list) -> str:
    # Group by subsystem, sort alphabetically within each group
    groups: dict[str, list] = defaultdict(list)
    for node in nodes:
        sub = node.get("properties", {}).get("subsystem", "")
        groups[sub].append(node)
    for sub in groups:
        groups[sub].sort(key=lambda n: n["id"])

    lines = ["<!-- NETJSON:REGISTRY:START -->"]

    for sub_key in SUBSYSTEM_ORDER:
        if sub_key not in groups:
            continue
        sub_label = SUBSYSTEM_LABELS.get(sub_key, sub_key)
        lines.append(f"\n**{sub_label}**\n")
        lines.append("| Tag | Device | Type | MAC Address | Serial Number |")
        lines.append("|-----|--------|------|-------------|---------------|")
        for node in groups[sub_key]:
            p = node.get("properties", {})
            doc = p.get("doc", "")
            tag = node["id"]
            label = node["label"]
            device_type = p.get("type") or "TBD"
            mac = p.get("mac_address") or "TBD"
            serial = p.get("serial_number") or "TBD"
            link = f"[{tag}]({doc})" if doc else tag
            lines.append(f"| {link} | {label} | {device_type} | {mac} | {serial} |")

    # Any nodes with unrecognised subsystem keys
    extras = [n for k, v in groups.items() if k not in SUBSYSTEM_ORDER for n in v]
    if extras:
        lines.append("\n**Other**\n")
        lines.append("| Tag | Device | Type | MAC Address | Serial Number |")
        lines.append("|-----|--------|------|-------------|---------------|")
        for node in sorted(extras, key=lambda n: n["id"]):
            p = node.get("properties", {})
            doc = p.get("doc", "")
            tag = node["id"]
            link = f"[{tag}]({doc})" if doc else tag
            lines.append(f"| {link} | {node['label']} | {p.get('type') or 'TBD'} | {p.get('mac_address') or 'TBD'} | {p.get('serial_number') or 'TBD'} |")

    lines.append("\n<!-- NETJSON:REGISTRY:END -->")
    return "\n".join(lines)


def update_registry(readme_path: Path, nodes: list, dry_run: bool = False) -> bool:
    if not readme_path.exists():
        print(f"  SKIP  {readme_path.name} — file not found")
        return False
    content = readme_path.read_text()
    original = content
    pat = r"<!-- NETJSON:REGISTRY:START -->.*?<!-- NETJSON:REGISTRY:END -->"
    if not re.search(pat, content, re.DOTALL):
        print(f"  WARN  {readme_path.name} — NETJSON:REGISTRY marker missing, skipped")
        return False
    content = re.sub(pat, render_registry_block(nodes), content, count=1, flags=re.DOTALL)
    if content == original:
        print(f"  OK    {readme_path.name} — no changes needed")
        return False
    if not dry_run:
        readme_path.write_text(content)
        print(f"  WROTE {readme_path.name}")
    else:
        print(f"  WOULD UPDATE {readme_path.name} (dry run)")
    return True


# ---------------------------------------------------------------------------
# File update
# ---------------------------------------------------------------------------

def update_file(md_path: Path, node: dict, dry_run: bool = False) -> bool:
    if not md_path.exists():
        print(f"  SKIP  {md_path.relative_to(REPO_ROOT)} — file not found")
        return False

    content = md_path.read_text()
    original = content

    # Update H1 title to "# TAG — Label"
    title = f"# {node['id']} — {node['label']}"
    content = re.sub(r"^# .+$", title, content, count=1, flags=re.MULTILINE)

    # Update info block
    pat_info = r"<!-- NETJSON:START -->.*?<!-- NETJSON:END -->"
    if re.search(pat_info, content, re.DOTALL):
        content = re.sub(pat_info, render_info_block(node), content, flags=re.DOTALL)
    else:
        print(f"  WARN  {md_path.name} — NETJSON:START marker missing, info block skipped")

    # Update interfaces block
    pat_iface = r"<!-- NETJSON:INTERFACES:START -->.*?<!-- NETJSON:INTERFACES:END -->"
    if re.search(pat_iface, content, re.DOTALL):
        content = re.sub(pat_iface, render_interfaces_block(node), content, flags=re.DOTALL)

    if content == original:
        print(f"  OK    {md_path.name} — no changes needed")
        return False

    if not dry_run:
        md_path.write_text(content)
        print(f"  WROTE {md_path.name}")
    else:
        print(f"  WOULD UPDATE {md_path.name} (dry run)")
    return True


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _collect_ip_map(nodes: list) -> dict[str, set[str]]:
    """Return {ip: {node_ids}} for every IP documented across all nodes."""
    ip_map: dict[str, set[str]] = defaultdict(set)
    for node in nodes:
        nid = node["id"]
        for addr in node.get("local_addresses", []):
            ip_map[addr.split("/")[0]].add(nid)
        for iface in node.get("properties", {}).get("interfaces", []):
            for addr in iface.get("addresses", []):
                ip_map[addr.split("/")[0]].add(nid)
    return ip_map


def validate(data: dict) -> tuple:
    errors = []
    warnings = []
    nodes = data.get("nodes", [])
    links = data.get("links", [])
    valid_ids = {n["id"] for n in nodes} | {"WAN"}

    # 1 — Unique node IDs
    ids = [n["id"] for n in nodes]
    seen = set()
    for nid in ids:
        if nid in seen:
            errors.append(f"Duplicate node ID: {nid}")
        seen.add(nid)

    # 2 — tag property matches node ID
    for node in nodes:
        tag = node.get("properties", {}).get("tag")
        if tag and tag != node["id"]:
            errors.append(
                f"[{node['id']}] 'tag' property '{tag}' does not match node ID"
            )

    # 3 — All doc paths exist on disk
    for node in nodes:
        doc = node.get("properties", {}).get("doc")
        if doc and not (REPO_ROOT / doc).exists():
            errors.append(f"[{node['id']}] doc path not found: {doc}")

    # 4 — All docs have NETJSON markers
    for node in nodes:
        doc = node.get("properties", {}).get("doc")
        if doc:
            path = REPO_ROOT / doc
            if path.exists():
                content = path.read_text()
                if "<!-- NETJSON:START -->" not in content:
                    warnings.append(
                        f"[{node['id']}] missing <!-- NETJSON:START --> in {Path(doc).name}"
                    )
                if "<!-- NETJSON:INTERFACES:START -->" not in content:
                    warnings.append(
                        f"[{node['id']}] missing <!-- NETJSON:INTERFACES:START --> in {Path(doc).name}"
                    )

    # 5 — Link source/target validity
    for link in links:
        src, tgt = link.get("source"), link.get("target")
        if src not in valid_ids:
            errors.append(f"Link source '{src}' is not a valid node ID")
        if tgt not in valid_ids:
            errors.append(f"Link target '{tgt}' is not a valid node ID")

    # 6 — Stale tag references in manual sections of device docs
    for node in nodes:
        doc = node.get("properties", {}).get("doc")
        if not doc:
            continue
        path = REPO_ROOT / doc
        if not path.exists():
            continue
        content = path.read_text()
        stripped = re.sub(r"<!-- NETJSON:START -->.*?<!-- NETJSON:END -->", "", content, flags=re.DOTALL)
        stripped = re.sub(r"<!-- NETJSON:INTERFACES:START -->.*?<!-- NETJSON:INTERFACES:END -->", "", stripped, flags=re.DOTALL)
        found_tags = set(TAG_PATTERN.findall(stripped))
        stale = found_tags - valid_ids - KNOWN_NON_TAGS
        for tag in sorted(stale):
            warnings.append(
                f"[{node['id']}] stale tag '{tag}' in manual section of {Path(doc).name}"
            )

    # 7 — H1 title matches expected format
    for node in nodes:
        doc = node.get("properties", {}).get("doc")
        if not doc:
            continue
        path = REPO_ROOT / doc
        if not path.exists():
            continue
        content = path.read_text()
        expected_title = f"# {node['id']} — {node['label']}"
        first_h1 = next((line for line in content.splitlines() if line.startswith("# ")), None)
        if first_h1 and first_h1 != expected_title:
            warnings.append(
                f"[{node['id']}] H1 title mismatch in {Path(doc).name}\n"
                f"    expected: {expected_title}\n"
                f"    found:    {first_h1}"
            )

    # 8 — IP uniqueness across all devices
    ip_map = _collect_ip_map(nodes)
    for ip, owners in ip_map.items():
        if len(owners) > 1:
            errors.append(f"Duplicate IP {ip} assigned to: {', '.join(sorted(owners))}")

    # 9 — local_addresses consistent with interface IPs
    for node in nodes:
        local_ips = {a.split("/")[0] for a in node.get("local_addresses", [])}
        iface_ips = set()
        for iface in node.get("properties", {}).get("interfaces", []):
            for addr in iface.get("addresses", []):
                iface_ips.add(addr.split("/")[0])
        missing_from_local = iface_ips - local_ips
        for ip in sorted(missing_from_local):
            warnings.append(
                f"[{node['id']}] interface IP {ip} not listed in local_addresses"
            )

    # 10 — management_url IP belongs to a known device
    all_ips: dict[str, str] = {}
    for node in nodes:
        nid = node["id"]
        for addr in node.get("local_addresses", []):
            all_ips[addr.split("/")[0]] = nid
        for iface in node.get("properties", {}).get("interfaces", []):
            for addr in iface.get("addresses", []):
                all_ips[addr.split("/")[0]] = nid
    for node in nodes:
        mgmt_url = node.get("properties", {}).get("management_url") or ""
        for ip in _IP_PAT.findall(mgmt_url):
            owner = all_ips.get(ip)
            if owner is None:
                warnings.append(
                    f"[{node['id']}] management_url references {ip} which is not documented on any device"
                )
            elif owner != node["id"]:
                warnings.append(
                    f"[{node['id']}] management_url references {ip} which belongs to {owner} "
                    f"— verify this is intentional (e.g. hosted service)"
                )

    return errors, warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv
    run_validate = "--validate" in sys.argv

    if not NETWORK_JSON.exists():
        print(f"ERROR: {NETWORK_JSON} not found")
        sys.exit(1)

    data = json.loads(NETWORK_JSON.read_text())
    nodes = data.get("nodes", [])
    print(f"Loaded {len(nodes)} nodes from {NETWORK_JSON.relative_to(REPO_ROOT)}\n")

    if run_validate:
        print("=== Validation ===")
        errors, warnings = validate(data)
        for msg in errors:
            print(f"  ERROR   {msg}")
        for msg in warnings:
            print(f"  WARNING {msg}")
        if not errors and not warnings:
            print("  All checks passed.")
        print()
        if errors:
            sys.exit(1)

    if "--validate" in sys.argv and "--dry-run" not in sys.argv and not any(
        a for a in sys.argv[1:] if a not in ("--validate", "--dry-run")
    ):
        if "--dry-run" not in sys.argv:
            return

    if dry_run:
        print("Dry run — no files will be written.\n")

    updated = 0
    skipped = 0
    for node in nodes:
        doc_rel = node.get("properties", {}).get("doc")
        if not doc_rel:
            print(f"[{node['id']}] SKIP — no 'doc' path in properties")
            skipped += 1
            continue
        md_path = REPO_ROOT / doc_rel
        print(f"[{node['id']}] {doc_rel}")
        if update_file(md_path, node, dry_run):
            updated += 1

    print(f"\n[README] README.md")
    if update_registry(REPO_ROOT / "README.md", nodes, dry_run):
        updated += 1

    action = "would update" if dry_run else "updated"
    print(f"\nDone — {action} {updated} file(s), skipped {skipped}.")


if __name__ == "__main__":
    main()
