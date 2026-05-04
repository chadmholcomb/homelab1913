# SEL RTAC 3505

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | RTAC-1 |
| **Manufacturer** | Schweitzer Engineering Laboratories |
| **Model** | RTAC 3505 |
| **Type** | Real-Time Automation Controller |
| **Segment** | Target Hardware |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **Management** | AcSELerator RTAC |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

The SEL RTAC 3505 is a Real-Time Automation Controller that functions as a protocol gateway, data concentrator, and automation platform. In energy management and power systems contexts it:

- Collects data from field devices (meters, relays) over multiple protocols simultaneously
- Translates between protocols (e.g., Modbus → DNP3, serial → Ethernet)
- Executes automation logic (AcSELerator RTAC scripts / IEC 61131 logic)
- Acts as a SCADA front-end concentrator

Will be tested against via DEV-1 (Arduino OPTA).

## Key Specs

- Multiple 10/100 Ethernet ports
- Serial ports: RS-232, RS-485 (COM1–COM4 depending on option cards)
- Supported protocols: DNP3 Master/Outstation, Modbus RTU/TCP Master/Slave, IEC 61850 Client/Server, SEL Fast Message, GOOSE, ICCP
- Real-time clock with IRIG-B / GPS sync support
- Configured via AcSELerator RTAC (Windows software)

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| ETH1 | ethernet | lan | TBD | Primary — NS-2 P4 |
| ETH2 | ethernet | lan | TBD | TBD |
| COM1 | rs232 | serial | TBD | TBD |
| COM2 | rs485 | serial | TBD | TBD |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **ETH1:** → NS-2 (USW-Pro-8-PoE 120W) Port P4
- **Serial COM1:** TBD
- **Serial COM2:** TBD

## Protocol Map

| Protocol | Role | Connected Device | Notes |
|----------|------|-----------------|-------|
| Modbus TCP | Client | MTR-1 (eGauge 4015) | TBD — register map |
| TBD | TBD | TBD | |

## Management Access

- **Web UI:** `http://<IP>` — AcSELerator RTAC web interface
- **AcSELerator RTAC:** SEL Windows application — project upload/download/monitoring
- **SSH/Telnet:** TBD

## Notes

TBD
