# MOD-1 — Cradlepoint IBR600

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | MOD-1 |
| **Manufacturer** | Cradlepoint |
| **Model** | IBR600 |
| **Type** | LTE Cellular Router |
| **Segment** | Development Environment |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | 00:30:44:70:3F:C5 |
| **Serial Number** | IMEI: 865 4930 4342 5942 |
| **Management** | NetCloud Manager |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Provides LTE cellular WAN connectivity for the development environment. Primary purpose is enabling remote administration and access to the lab without requiring a static IP or on-site presence.

## Key Specs

- LTE Cat 6 (model variant dependent)
- 1x GbE WAN, 4x GbE LAN
- Remote management via Cradlepoint NetCloud Manager
- Built-in firewall and VPN support
- Operating temperature: -20°C to 60°C

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| lte0 | lte | wan | TBD | Primary LTE uplink — remote admin access |
| eth0 | ethernet | lan | TBD | LAN to NS-1 P1 |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **WAN:** LTE cellular antenna
- **eth0:** → NS-1 (USW-Lite-8-PoE) Port P1

## Management Access

- **NetCloud Manager:** TBD (org/URL)
- **Local UI:** `http://192.168.0.1` (default) or assigned LAN IP
- **Default credentials:** See device label or NetCloud Manager

## Notes

TBD
