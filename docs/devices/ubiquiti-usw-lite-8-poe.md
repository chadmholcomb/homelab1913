# Ubiquiti USW-Lite-8-PoE

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | NS-1 |
| **Manufacturer** | Ubiquiti |
| **Model** | USW-Lite-8-PoE |
| **Type** | Managed Layer 2 PoE Switch |
| **Segment** | Development Environment |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **Management** | UniFi Network Controller |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Core switch for the development environment. Connects all development-side devices and provides the cross-connect uplink into the Energy Management Assembly at NS-2.

## Key Specs

- 8x GbE ports total
- Ports 1–4: PoE+ (IEEE 802.3af/at), 52W total budget
- Ports 5–8: non-PoE
- Managed via UniFi Network Controller
- Fanless, wall/desktop mountable

## Port Map

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| P1 | ethernet | uplink | TBD | MOD-1 LAN |
| P2 | ethernet | access | TBD | SRV-1 |
| P3 | ethernet | access | TBD | TBD |
| P4 | ethernet | access | TBD | TBD |
| P5 | ethernet | access | TBD | TBD |
| P6 | ethernet | access | TBD | TBD |
| P7 | ethernet | access | TBD | TBD |
| P8 | ethernet | trunk | TBD | Cross-connect to NS-2 P1 |
<!-- NETJSON:INTERFACES:END -->

## Management Access

- **UniFi Controller:** TBD (controller IP/URL)
- **SSH:** `ssh admin@<IP>`

## Notes

TBD
