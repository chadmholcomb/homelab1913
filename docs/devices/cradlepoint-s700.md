# Cradlepoint S700

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | MOD-2 |
| **Manufacturer** | Cradlepoint |
| **Model** | S700 |
| **Type** | 5G/LTE Branch Router |
| **Segment** | Energy Management Assembly |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **Management** | NetCloud Manager |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Provides independent LTE/5G WAN connectivity for the Energy Management Assembly. Keeps the EMA network segment isolated from the development environment while still allowing remote access via NetCloud Manager — mirrors a real field-deployed site's WAN connectivity.

## Key Specs

- 5G sub-6 GHz / LTE fallback
- Multiple GbE LAN ports
- Advanced SD-WAN and routing features
- NetCloud Manager cloud management
- DIN-rail mountable (with bracket)

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| lte0 | lte | wan | TBD | Primary LTE/5G uplink for EMA assembly |
| eth0 | ethernet | lan | TBD | LAN to NS-2 P2 |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **WAN:** LTE/5G cellular antenna
- **eth0:** → NS-2 (USW-Pro-8-PoE 120W) Port P2

## Management Access

- **NetCloud Manager:** TBD
- **Local UI:** TBD

## Notes

TBD
