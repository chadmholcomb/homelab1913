# DEV-1 — Wago 750-8212

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | DEV-1 |
| **Manufacturer** | Wago |
| **Model** | 750-8212 |
| **Type** | Programmable Logic Controller |
| **Subsystem** | Target Hardware |
| **Hostname** | TBD |
| **IP Address** | TBD |
| **MAC Address** | TBD |
| **Serial Number** | TBD |
| **Management** | CODESYS / Web UI |
| **Management URL** | TBD |
<!-- NETJSON:END -->

## Role

Wago PFC200 programmable logic controller used as a test and simulation device in the Target Hardware subsystem. Connected to the Development switch (NS-1) for programming and network communication. Intended to act as a programmable client/master to exercise and validate other target hardware in the lab (RTAC-1, MET-1).

## Key Specs

- Wago 750-8212 PFC200 Controller
- Dual-core ARM Cortex-A8 processor (Linux-based runtime)
- Runs CODESYS 3 runtime
- 2x RJ45 Ethernet ports (ETH1, ETH2) — supports switch or independent addressing
- Supports Modbus TCP (master/slave), EtherNet/IP, PROFIBUS, CANopen (via fieldbus modules)
- DIN-rail mountable with 750/753 series I/O module expansion
- Web-based management UI (WBM)

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| ETH1 | ethernet | lan | TBD | NS-1 P7 |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **ETH1:** → NS-1 Port P7 (primary network / programming)

## Protocol Map

| Protocol | Role | Notes |
|----------|------|-------|
| Modbus TCP | Master/Client | TBD — polling RTAC-1 or MET-1 |
| EtherNet/IP | TBD | TBD |
| CODESYS runtime | Programming | Via CODESYS Development System over ETH1 |
| Web UI (WBM) | Management | Browser-based configuration at device IP |

## Management Access

- **Web-Based Management (WBM):** `http://<device-ip>` — device IP TBD
- **CODESYS Development System:** Connect to ETH1 over the lab network

## Notes

TBD — I/O module configuration and test programs not yet defined.
