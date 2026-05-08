# NS-2 — Ubiquiti USW-Pro-8-PoE 120W

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | NS-2 |
| **Manufacturer** | Ubiquiti |
| **Model** | USW-Pro-8-PoE |
| **Type** | Managed Layer 2/3 PoE Switch |
| **Subsystem** | Energy Management Assembly |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | TBD |
| **Serial Number** | TBD |
| **Management** | UniFi Network Controller |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Core switch for the Energy Management Assembly. Distributes PoE power and network connectivity to all EMA and target hardware devices. Receives uplinks from both MOD-2 (WAN) and NS-1 (cross-connect from the development environment).

## Key Specs

- 8x GbE PoE+ ports (IEEE 802.3af/at/bt), 120W total budget
- 2x SFP+ 10G uplink ports
- Layer 2/3 managed (static routing capable)
- Managed via UniFi Network Controller
- Fanless

## Port Map

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| P1 | ethernet | access | TBD | PC-2 (X4LAN) |
| P2 | ethernet | access | TBD | TBD |
| P3 | ethernet | access | TBD | TBD |
| P4 | ethernet | access | TBD | RTAC-1 (ETH1) |
| P5 | ethernet | access | TBD | MET-1 (ETH0) |
| P6 | ethernet | access | TBD | AP-2 |
| P7 | ethernet | access | TBD | DEV-1 (planned) |
| P8 | ethernet | uplink | TBD | MOD-2 LAN |
| SFP1 | sfp+ | reserved | TBD | TBD |
| SFP2 | sfp+ | reserved | TBD | TBD |
<!-- NETJSON:INTERFACES:END -->

## Management Access

- **UniFi Controller:** TBD (controller IP/URL)
- **SSH:** `ssh admin@<IP>`

## Notes

TBD
