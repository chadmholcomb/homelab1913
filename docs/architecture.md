# Lab Architecture

## Network Subsystems

The lab is divided into three logical subsystems connected through a pair of managed switches.

### Development Subsystem

| Tag | Device | IP | Role |
|-----|--------|----|------|
| [MOD-1](devices/mod-1.md) | Cradlepoint IBR600 | 172.22.1.1 | LTE WAN uplink, remote access gateway |
| [NS-1](devices/ns-1.md) | Ubiquiti USW-Lite-8-PoE | 172.22.1.3 | Layer 2 managed switch |
| [PC-1](devices/pc-1.md) | Fanless PC | 172.22.1.40 | Linux tooling and log aggregation host |

MOD-1 (IBR600) provides LTE connectivity managed via NetCloud Manager, enabling remote SSH/VPN access without a fixed IP. NS-1 (USW-Lite-8-PoE) connects development devices and provides a cross-connect uplink to NS-2 on the EMA subsystem.

---

### Energy Management Assembly

| Tag | Device | IP | Role |
|-----|--------|----|------|
| [MOD-2](devices/mod-2.md) | Cradlepoint S700 | TBD | LTE/5G WAN uplink |
| [NS-2](devices/ns-2.md) | Ubiquiti USW-Pro-8-PoE 120W | TBD | Core managed PoE switch |
| [PC-2](devices/pc-2.md) | Phoenix Contact PC | TBD | Industrial controller / automation host |
| [AP-2](devices/ap-2.md) | WiFi Access Point | TBD | Wireless access for EMA segment |

The EMA assembly is a self-contained unit on the gold-plate panel simulating a field-deployed energy management system. MOD-2 (S700) provides an independent LTE uplink separate from the development environment.

---

### Target Hardware

| Tag | Device | IP | Protocols |
|-----|--------|-----|-----------|
| [RTAC-1](devices/rtac-1.md) | SEL RTAC 3505 | TBD | DNP3, Modbus TCP/RTU, IEC 61850, SEL protocol |
| [MET-1](devices/met-1.md) | eGauge 4015 | TBD | Modbus TCP, HTTP REST API |
| [DEV-1](devices/dev-1.md) | Arduino OPTA | TBD | Modbus RTU/TCP _(test device — WIP)_ |

---

## Physical Topology

```
        [Internet / LTE]
              |           |
          [MOD-1]     [MOD-2]
        Modem/Router  Modem/Router
              |           |
          [NS-1]  ←C-03→ [NS-2]
          Switch          Switch
            |          /   |   |   \
         [PC-1]   [PC-2] [RTAC-1] [MET-1] [AP-2]
        Linux PC  Linux PC  RTAC  Power Meter WiFi AP
                                    ↑
                                 [DEV-1]
                                 PLC (WIP)
```

---

## Cable Schedule

> Update **Length** and **Cable Type** as cables are measured and labeled.
> Cable IDs (C-xx) are used as references in port maps and physical labels.

| ID | Connection | A-End | A-Port | B-End | B-Port | Length | Cable Type | Notes |
|----|-----------|-------|--------|-------|--------|--------|------------|-------|
| C-01 | ETH | MOD-1 | LAN | NS-1 | P1 | TBD | TBD | Dev environment LAN uplink |
| C-02 | ETH | NS-1 | P2 | PC-1 | LAN1 | TBD | TBD | |
| C-03 | ETH | MOD-2 | LAN | NS-2 | P8 | TBD | TBD | EMA assembly LAN uplink |
| C-04 | ETH | NS-2 | P1 | PC-2 | X4LAN | TBD | TBD | |
| C-05 | ETH | NS-2 | P4 | RTAC-1 | ETH1 | TBD | TBD | |
| C-06 | ETH | NS-2 | P5 | MET-1 | ETH0 | TBD | TBD | |
| C-07 | ETH+PoE | NS-2 | P6 | AP-2 | eth0 | TBD | TBD | PoE powered from NS-2 |
| C-08 | ETH | NS-2 | P7 | DEV-1 | ETH0 | TBD | TBD | Planned — not yet connected |
| L-01 | LTE | WAN | — | MOD-1 | LTE | N/A | Cellular | Dev environment WAN |
| L-02 | LTE | WAN | — | MOD-2 | LTE | N/A | Cellular | EMA assembly WAN |

---

## Power Distribution

| PSU | Voltage | Location | Powers |
|-----|---------|----------|--------|
| Mean Well NDR-120-45 | 48V DC | Gold plate (EMA) | TBD |
| Mean Well NDR-120-24 | 24V DC | Bottom DIN rail | TBD |

---

## Connection Types

Standard line styles used in topology diagrams throughout this repo.

| Mermaid Style | Medium | Port Labels | Notes |
|---------------|--------|-------------|-------|
| `A --> B` solid arrow | Ethernet | Yes — `SRC:port -- DST:port` | Physical copper cable |
| `A ==> B` thick arrow | Cellular / LTE / 5G | No | Wireless WAN — no physical cable or port |
| `A -.-> B` dotted arrow | WiFi | No | Wireless LAN |
| `A --o B` circle-end | RS-485 / Serial | Yes | Physical serial cable |
| `A -.-> B` dotted arrow | Planned / inactive | Yes | Link defined but not yet physically connected |

> WiFi and Serial styles are reserved for future use in the EMA and Target Hardware subsystems.

---

## Protocol Overview

TBD — to be filled in as lab configuration is finalized.
