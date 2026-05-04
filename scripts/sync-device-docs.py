#!/usr/bin/env python3
"""
sync-device-docs.py

Reads docs/network.json (NetJSON NetworkGraph) and updates the
<!-- NETJSON:START/END --> and <!-- NETJSON:INTERFACES:START/END --> sections
in each device's markdown file with current values from the JSON.

Edit docs/network.json to update device info, then run this script to
propagate those changes to all device documentation files.

Usage:
    python3 scripts/sync-device-docs.py [--dry-run]
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NETWORK_JSON = REPO_ROOT / "docs" / "network.json"

SEGMENT_LABELS = {
    "development": "Development Environment",
    "ema": "Energy Management Assembly",
    "target": "Target Hardware",
}


def render_info_block(node: dict) -> str:
    p = node.get("properties", {})
    addresses = node.get("local_addresses", [])
    rows = [
        ("Tag",            node["id"]),
        ("Manufacturer",   p.get("manufacturer") or "TBD"),
        ("Model",          p.get("model") or "TBD"),
        ("Type",           p.get("type") or "TBD"),
        ("Segment",        SEGMENT_LABELS.get(p.get("segment", ""), p.get("segment") or "TBD")),
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


def update_file(md_path: Path, node: dict, dry_run: bool = False) -> bool:
    if not md_path.exists():
        print(f"  SKIP  {md_path.relative_to(REPO_ROOT)} — file not found")
        return False

    content = md_path.read_text()
    original = content

    pat_info = r"<!-- NETJSON:START -->.*?<!-- NETJSON:END -->"
    pat_iface = r"<!-- NETJSON:INTERFACES:START -->.*?<!-- NETJSON:INTERFACES:END -->"

    if re.search(pat_info, content, re.DOTALL):
        content = re.sub(pat_info, render_info_block(node), content, flags=re.DOTALL)
    else:
        print(f"  WARN  {md_path.name} — NETJSON:START marker missing, info block not updated")

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


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("Dry run — no files will be written.\n")

    if not NETWORK_JSON.exists():
        print(f"ERROR: {NETWORK_JSON} not found")
        sys.exit(1)

    data = json.loads(NETWORK_JSON.read_text())
    nodes = data.get("nodes", [])
    print(f"Loaded {len(nodes)} nodes from {NETWORK_JSON.relative_to(REPO_ROOT)}\n")

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

    action = "would update" if dry_run else "updated"
    print(f"\nDone — {action} {updated} file(s), skipped {skipped}.")


if __name__ == "__main__":
    main()
