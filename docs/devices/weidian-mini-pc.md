# Weidian Mini PC

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | SRV-1 |
| **Manufacturer** | Weidian |
| **Model** | TBD |
| **Type** | Industrial Fanless Mini PC |
| **Segment** | Development Environment |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **Management** | SSH |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

General-purpose Linux environment for tooling development and log aggregation. Serves as the primary workstation on the lab bench for:

- Writing and testing protocol scripts (Modbus, DNP3, etc.)
- Running log collection and aggregation agents
- Development of observability tooling
- Ad-hoc device testing and commissioning

## Key Specs

- TBD — CPU, RAM, storage
- Fanless industrial form factor
- Multiple GbE Ethernet ports
- USB and serial interfaces

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| eth0 | ethernet | lan | TBD | NS-1 P2 |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **eth0:** → NS-1 (USW-Lite-8-PoE) Port P2

## Installed Software

| Tool | Purpose |
|------|---------|
| TBD | TBD |

## Management Access

- **SSH:** `ssh <user>@<IP>`
- **Console:** TBD (serial or direct)

## Notes

TBD
