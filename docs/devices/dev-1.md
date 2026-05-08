# DEV-1 — Arduino OPTA

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | DEV-1 |
| **Manufacturer** | Arduino |
| **Model** | OPTA |
| **Type** | Industrial Programmable Logic Controller |
| **Subsystem** | Target Hardware |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | TBD |
| **Serial Number** | TBD |
| **Management** | Arduino IDE / Arduino Cloud |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Industrial-grade Arduino used as a test and simulation device. Intended to act as a programmable client/master to exercise and validate the target hardware in this lab:

- **PC-2** (Phoenix Contact PC) — TBD protocol/connection
- **RTAC-1** (SEL RTAC 3505) — TBD protocol/connection
- **MET-1** (eGauge 4015) — TBD protocol/connection

> This device is a work in progress. Connections and test programs are not yet defined.

## Key Specs

- STM32H747 dual-core processor (Cortex-M7 + M4)
- 8x digital I/O (relay outputs up to 250VAC/2A)
- 4x analog inputs (0–10V or 4–20mA)
- 1x 10/100 Ethernet port
- 1x RS-485 port
- USB-C programming port
- DIN-rail mountable
- Operating temperature: -20°C to 50°C

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| ETH0 | ethernet | lan | TBD | NS-2 P7 (planned) |
| RS485 | rs485 | serial | TBD | TBD — connection to PC-2 / RTAC-1 / MET-1 (planned) |
<!-- NETJSON:INTERFACES:END -->

## Planned Connections

| Interface | Target | Protocol | Purpose |
|-----------|--------|----------|---------|
| ETH0 / RS-485 | PC-2 | TBD | TBD |
| ETH0 / RS-485 | RTAC-1 | TBD | TBD |
| ETH0 | MET-1 | Modbus TCP | TBD |

## Management Access

- **Arduino IDE:** USB-C programming connection
- **Arduino Cloud:** TBD (if cloud agent configured)

## Notes

Connections and test programs to be built out. All interface and protocol details are TBD pending lab configuration decisions.
