# MET-1 — eGauge 4015

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | MET-1 |
| **Manufacturer** | eGauge Systems |
| **Model** | EG4015 |
| **Type** | Revenue-Grade Power Meter |
| **Subsystem** | Target Hardware |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | TBD |
| **Serial Number** | TBD |
| **Management** | Web UI / REST API |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Revenue-grade power meter providing real-time and historical energy data. Primary data source for the energy management system — reports power, voltage, current, power factor, and energy totals per circuit. Will be tested against via DEV-1 (Arduino OPTA).

## Key Specs

- Revenue-grade accuracy (ANSI C12.20 Class 0.2)
- Up to 12 CT (current transformer) input channels
- Voltage inputs: up to 600V L-L
- 1x GbE Ethernet port
- Internal flash storage — years of 1-second resolution historical data
- Real-time clock (battery backed)

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| ETH0 | ethernet | lan | TBD | NS-1 P2 |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **ETH0:** → NS-2 (USW-Pro-8-PoE 120W) Port P5
- **CT Inputs (I1–I12):** TBD — CT wiring map to be documented
- **Voltage Inputs (V1–V3):** TBD

## API / Data Access

| Method | Details | Notes |
|--------|---------|-------|
| Web UI | `http://<IP>` | Browser dashboard — real-time and historical data |
| HTTP GET | `http://<IP>/api?` | JSON API — real-time register reads |
| Modbus TCP | Port 502 | Register map TBD |
| XML Push | TBD | Configurable push to remote server |

## Modbus Register Map

TBD — to be documented once CT wiring is confirmed.

## CT Wiring Map

| Channel | Circuit | CT Ratio | Notes |
|---------|---------|----------|-------|
| I1 | TBD | TBD | |
| I2 | TBD | TBD | |
| I3 | TBD | TBD | |

## Notes

TBD
