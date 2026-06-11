# FMC-1 — E-link LNK-IMC1200GP-SFP

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | FMC-1 |
| **Manufacturer** | E-link |
| **Model** | LNK-IMC1200GP-SFP |
| **Type** | Fiber Media Converter |
| **Subsystem** | Development Subsystem |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | TBD |
| **Serial Number** | TBD |
| **Management** | TBD |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

DEV-side fiber media converter. Bridges the copper Ethernet segment of the Development Subsystem (NS-1) to the OS2 single-mode fiber run that cross-connects to the EMA Subsystem (NS-2 via FMC-2). Physically DIN-rail mounted in the Development assembly.

## Key Specs

- Model: E-link LNK-IMC1200GP-SFP
- SFP transceiver: 10Gtek 1000Base-SX (850 nm)
- Copper side: 10/100/1000BASE-T RJ45
- Fiber side: LC duplex SFP socket
- Form factor: DIN-rail
- Power: 24 Vdc DIN-rail PSU

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| ETH | ethernet | lan | TBD | NS-1 P8 — copper uplink to DEV switch |
| SFP | sfp | fiber | TBD | FMC-2 SFP — OS2 LC duplex, 10Gtek 1000Base-SX |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **ETH:** → NS-1 Port P8 (copper patch)
- **SFP:** → FMC-2 SFP (OS2 LC duplex fiber patch)

## Protocol Map

| Protocol | Role | Notes |
|----------|------|-------|
| Ethernet (Layer 1 bridge) | Transparent | No IP stack — media conversion only |

## Management Access

Unmanaged — no IP address or management interface.

## Notes

SFP transceiver is a 10Gtek 1000Base-SX module seated in the SFP socket. The fiber patch between FMC-1 and FMC-2 is an OS2 LC/UPC-LC/UPC duplex cable.
