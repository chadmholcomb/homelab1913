# FMC-2 — E-link LNK-IMC1200GP-SFP

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | FMC-2 |
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

EMA-side fiber media converter. Bridges the OS2 single-mode fiber run from the Development Subsystem (FMC-1) to the copper Ethernet segment of the Energy Management Assembly (NS-2). Physically located in the Development assembly DIN-rail alongside FMC-1.

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
| SFP | sfp | fiber | TBD | FMC-1 SFP — OS2 LC duplex, 10Gtek 1000Base-SX |
| ETH | ethernet | lan | TBD | NS-2 P8 — copper to EMA switch |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **SFP:** → FMC-1 SFP (OS2 LC duplex fiber patch)
- **ETH:** → NS-2 Port P8 (copper patch)

## Protocol Map

| Protocol | Role | Notes |
|----------|------|-------|
| Ethernet (Layer 1 bridge) | Transparent | No IP stack — media conversion only |

## Management Access

Unmanaged — no IP address or management interface.

## Notes

Physically co-located in the Development subsystem DIN rail even though its copper port terminates at NS-2 (EMA). SFP transceiver is a 10Gtek 1000Base-SX module. The fiber patch between FMC-1 and FMC-2 is an OS2 LC/UPC-LC/UPC duplex cable.
