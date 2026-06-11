# PC-2 — Phoenix Contact VL3 UPC 2440

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | PC-2 |
| **Manufacturer** | Phoenix Contact |
| **Model** | VL3 UPC 2440 |
| **Type** | Industrial DIN-Rail PC |
| **Subsystem** | Energy Management Assembly |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | CC:CC:EA:71:CB:50 |
| **Serial Number** | E254425853 |
| **Management** | TBD |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Industrial PC mounted on the DIN rail within the Energy Management Assembly. Runs control and automation software as would be found in a field-deployed energy management system. Intended as the primary automation host within the EMA assembly. Will be tested against via DEV-1 (Arduino OPTA).

## Key Specs

- TBD — model, CPU, RAM, storage
- DIN-rail mountable
- Extended temperature range
- Multiple I/O and communication interfaces

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| X4LAN | ethernet | lan | TBD | NS-2 P1 — primary LAN (MAC CC:CC:EA:71:CB:50) |
| X5LAN | ethernet | lan | TBD | Secondary LAN (MAC CC:CC:EA:71:CB:51) — TBD |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **eth0:** → NS-2 (USW-Pro-8-PoE 120W) Port P3
- **Serial / I/O:** TBD

## Management Access

- **SSH / RDP:** TBD
- **Local console:** TBD

## Notes

TBD — model number to be confirmed.
