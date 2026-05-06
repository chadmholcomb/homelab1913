# Lab Architecture

## Network Segments

The lab is divided into three logical segments connected through a pair of managed switches.

### Development Environment

| Tag | Device | IP | Role |
|-----|--------|----|------|
| [MOD-1](devices/cradlepoint-ibr600.md) | Cradlepoint IBR600 | 172.22.1.1 | LTE WAN uplink, remote access gateway |
| [NS-1](devices/ubiquiti-usw-lite-8-poe.md) | Ubiquiti USW-Lite-8-PoE | 172.22.1.3 | Layer 2 managed switch |
| [PC-1](devices/weidian-mini-pc.md) | Fanless PC | 172.22.1.40 | Linux tooling and log aggregation host |

MOD-1 (IBR600) provides LTE connectivity managed via NetCloud Manager, enabling remote SSH/VPN access without a fixed IP. NS-1 (USW-Lite-8-PoE) connects development devices and provides a cross-connect uplink to NS-2 on the EMA assembly.

---

### Energy Management Assembly

| Tag | Device | IP | Role |
|-----|--------|----|------|
| [MOD-2](devices/cradlepoint-s700.md) | Cradlepoint S700 | TBD | LTE/5G WAN uplink |
| [NS-2](devices/ubiquiti-usw-pro-8-poe.md) | Ubiquiti USW-Pro-8-PoE 120W | TBD | Core managed PoE switch |
| [PC-2](devices/phoenix-contact-pc.md) | Phoenix Contact PC | TBD | Industrial controller / automation host |
| [AP-2](devices/wifi-ap.md) | WiFi Access Point | TBD | Wireless access for EMA segment |

The EMA assembly is a self-contained unit on the gold-plate panel simulating a field-deployed energy management system. MOD-2 (S700) provides an independent LTE uplink separate from the development environment.

---

### Target Hardware

| Tag | Device | IP | Protocols |
|-----|--------|-----|-----------|
| [RTAC-1](devices/sel-rtac-3505.md) | SEL RTAC 3505 | TBD | DNP3, Modbus TCP/RTU, IEC 61850, SEL protocol |
| [MET-1](devices/egauge-4015.md) | eGauge 4015 | TBD | Modbus TCP, HTTP REST API |
| [DEV-1](devices/arduino-opta.md) | Arduino OPTA | TBD | Modbus RTU/TCP _(test device — WIP)_ |

---

## Physical Topology

```
          [Internet / LTE]
               |          |
           [MOD-1]    [MOD-2]
           IBR600       S700
               |          |
           [NS-1]  ←→  [NS-2]
         USW-Lite      USW-Pro
             |        /  |  |  \
          [PC-1]  [PC-2][RTAC-1][MET-1][AP-2]
        Fanless PC PHX PC RTAC  eGauge  WiFi
                              ↑
                          [DEV-1]
                          OPTA (WIP)
```

---

## Power Distribution

| PSU | Voltage | Location | Powers |
|-----|---------|----------|--------|
| Mean Well NDR-120-45 | 48V DC | Gold plate (EMA) | TBD |
| Mean Well NDR-120-24 | 24V DC | Bottom DIN rail | TBD |

---

## Protocol Overview

TBD — to be filled in as lab configuration is finalized.
