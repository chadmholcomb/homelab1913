# WiFi Access Point

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | AP-1 |
| **Manufacturer** | TBD |
| **Model** | TBD |
| **Type** | Wireless Access Point |
| **Segment** | Energy Management Assembly |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **Management** | TBD |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Provides wireless connectivity within the Energy Management Assembly segment. Allows wireless devices and laptops to connect to the EMA network without a wired connection.

## Key Specs

- TBD — 802.11 standard, frequency bands, spatial streams
- PoE powered from NS-2
- TBD — management platform (UniFi, standalone, etc.)

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| eth0 | ethernet | uplink | TBD | PoE uplink to NS-2 P6 |
| wlan0 | wifi | ap | TBD | SSID TBD |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **eth0:** → NS-2 (USW-Pro-8-PoE 120W) Port P6 (PoE powered)

## Wireless Configuration

| SSID | Band | Security | VLAN | Notes |
|------|------|----------|------|-------|
| TBD | TBD | TBD | TBD | |

## Management Access

- TBD

## Notes

Model to be confirmed. Update `manufacturer`, `model`, and `management_platform` in `docs/network.json` once confirmed, then run `python3 scripts/sync-device-docs.py`.
