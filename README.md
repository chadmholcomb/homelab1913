# Home Networking and Controls Development Lab

Documentation and observability repository for an industrial automation and energy management development lab.

## Lab Diagram

> Click any device node to open its documentation. Port labels show switch port assignments.

```mermaid
graph LR
    WAN(["Internet / LTE"])

    subgraph DEV["Development Environment"]
        MOD1["MOD-1\nCradlepoint IBR600"]
        NS1["NS-1\nUSW-Lite-8-PoE\n8×GbE · 52W PoE"]
        SRV1["SRV-1\nWeidian Mini PC"]
    end

    subgraph EMA["Energy Management Assembly"]
        MOD2["MOD-2\nCradlepoint S700"]
        NS2["NS-2\nUSW-Pro-8-PoE 120W\n8×GbE · 120W PoE · 2×SFP+"]
        IPC1["IPC-1\nPhoenix Contact PC"]
        AP1["AP-1\nWiFi Access Point"]
    end

    subgraph TGT["Target Hardware"]
        RTAC1["RTAC-1\nSEL RTAC 3505"]
        MTR1["MTR-1\neGauge 4015"]
        DEV1["DEV-1\nArduino OPTA\n(WIP)"]
    end

    WAN -->|LTE| MOD1
    WAN -->|LTE| MOD2
    MOD1 -->|"LAN → P1"| NS1
    NS1 -->|"P2"| SRV1
    NS1 -->|"P8 ↔ P1"| NS2
    MOD2 -->|"LAN → P2"| NS2
    NS2 -->|"P3"| IPC1
    NS2 -->|"P4"| RTAC1
    NS2 -->|"P5"| MTR1
    NS2 -->|"P6"| AP1
    NS2 -.->|"P7 planned"| DEV1

    click MOD1 "docs/devices/cradlepoint-ibr600.md"
    click MOD2 "docs/devices/cradlepoint-s700.md"
    click NS1 "docs/devices/ubiquiti-usw-lite-8-poe.md"
    click NS2 "docs/devices/ubiquiti-usw-pro-8-poe.md"
    click SRV1 "docs/devices/weidian-mini-pc.md"
    click IPC1 "docs/devices/phoenix-contact-pc.md"
    click AP1 "docs/devices/wifi-ap.md"
    click RTAC1 "docs/devices/sel-rtac-3505.md"
    click MTR1 "docs/devices/egauge-4015.md"
    click DEV1 "docs/devices/arduino-opta.md"
```

## Device Registry

| Tag | Device | Type | Segment |
|-----|--------|------|---------|
| [MOD-1](docs/devices/cradlepoint-ibr600.md) | Cradlepoint IBR600 | LTE Router | Development |
| [SRV-1](docs/devices/weidian-mini-pc.md) | Weidian Mini PC | Linux Server | Development |
| [NS-1](docs/devices/ubiquiti-usw-lite-8-poe.md) | Ubiquiti USW-Lite-8-PoE | Managed Switch | Development |
| [MOD-2](docs/devices/cradlepoint-s700.md) | Cradlepoint S700 | 5G/LTE Router | EMA Assembly |
| [NS-2](docs/devices/ubiquiti-usw-pro-8-poe.md) | Ubiquiti USW-Pro-8-PoE 120W | Managed Switch | EMA Assembly |
| [IPC-1](docs/devices/phoenix-contact-pc.md) | Phoenix Contact PC | Industrial PC | EMA Assembly |
| [AP-1](docs/devices/wifi-ap.md) | WiFi Access Point | Wireless AP | EMA Assembly |
| [RTAC-1](docs/devices/sel-rtac-3505.md) | SEL RTAC 3505 | Automation Controller | Target Hardware |
| [MTR-1](docs/devices/egauge-4015.md) | eGauge 4015 | Power Meter | Target Hardware |
| [DEV-1](docs/devices/arduino-opta.md) | Arduino OPTA | Industrial PLC / Test Device | Target Hardware |

## Repository Structure

```
docs/
  network.json       — NetJSON source of truth for all device/network config
  architecture.md    — Network architecture and segment details
  devices/           — Per-device documentation (generated sections synced from network.json)
observability/
  logging.md         — Log collection strategy
  monitoring.md      — Monitoring setup
scripts/
  sync-device-docs.py  — Propagates network.json changes to device markdown files
  collect-logs.sh      — Log collection automation
```

> To update device network config: edit `docs/network.json`, then run `python3 scripts/sync-device-docs.py`.
