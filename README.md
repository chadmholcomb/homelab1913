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
        PC1["PC-1\nFanless PC"]
    end

    subgraph EMA["Energy Management Assembly"]
        MOD2["MOD-2\nCradlepoint S700"]
        NS2["NS-2\nUSW-Pro-8-PoE 120W\n8×GbE · 120W PoE · 2×SFP+"]
        PC2["PC-2\nPhoenix Contact PC"]
        AP2["AP-2\nWiFi Access Point"]
    end

    subgraph TGT["Target Hardware"]
        RTAC1["RTAC-1\nSEL RTAC 3505"]
        MET1["MET-1\neGauge 4015"]
        DEV1["DEV-1\nArduino OPTA\n(WIP)"]
    end

    WAN -->|LTE| MOD1
    WAN -->|LTE| MOD2
    MOD1 -->|"LAN → P1"| NS1
    NS1 -->|"P2"| PC1
    NS1 -->|"P8 ↔ P1"| NS2
    MOD2 -->|"LAN → P2"| NS2
    NS2 -->|"P3"| PC2
    NS2 -->|"P4"| RTAC1
    NS2 -->|"P5"| MET1
    NS2 -->|"P6"| AP2
    NS2 -.->|"P7 planned"| DEV1

    click MOD1 "docs/devices/cradlepoint-ibr600.md"
    click MOD2 "docs/devices/cradlepoint-s700.md"
    click NS1 "docs/devices/ubiquiti-usw-lite-8-poe.md"
    click NS2 "docs/devices/ubiquiti-usw-pro-8-poe.md"
    click PC1 "docs/devices/weidian-mini-pc.md"
    click PC2 "docs/devices/phoenix-contact-pc.md"
    click AP2 "docs/devices/wifi-ap.md"
    click RTAC1 "docs/devices/sel-rtac-3505.md"
    click MET1 "docs/devices/egauge-4015.md"
    click DEV1 "docs/devices/arduino-opta.md"
```

## Device Registry

| Tag | Device | Type | Segment | MAC Address | Serial Number |
|-----|--------|------|---------|-------------|---------------|
| [MOD-1](docs/devices/cradlepoint-ibr600.md) | Cradlepoint IBR600 | LTE Router | Development | TBD | TBD |
| [PC-1](docs/devices/weidian-mini-pc.md) | Fanless PC | Linux Server | Development | TBD | TBD |
| [NS-1](docs/devices/ubiquiti-usw-lite-8-poe.md) | Ubiquiti USW-Lite-8-PoE | Managed Switch | Development | TBD | TBD |
| [MOD-2](docs/devices/cradlepoint-s700.md) | Cradlepoint S700 | 5G/LTE Router | EMA Assembly | TBD | TBD |
| [NS-2](docs/devices/ubiquiti-usw-pro-8-poe.md) | Ubiquiti USW-Pro-8-PoE 120W | Managed Switch | EMA Assembly | TBD | TBD |
| [PC-2](docs/devices/phoenix-contact-pc.md) | Phoenix Contact PC | Industrial PC | EMA Assembly | TBD | TBD |
| [AP-2](docs/devices/wifi-ap.md) | WiFi Access Point | Wireless AP | EMA Assembly | TBD | TBD |
| [RTAC-1](docs/devices/sel-rtac-3505.md) | SEL RTAC 3505 | Automation Controller | Target Hardware | TBD | TBD |
| [MET-1](docs/devices/egauge-4015.md) | eGauge 4015 | Power Meter | Target Hardware | TBD | TBD |
| [DEV-1](docs/devices/arduino-opta.md) | Arduino OPTA | Industrial PLC / Test Device | Target Hardware | TBD | TBD |

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
