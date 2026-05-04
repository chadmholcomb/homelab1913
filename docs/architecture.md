# Lab Architecture

## Network Segments

The lab is divided into three logical segments connected through a pair of managed switches.

### Development Environment

| Device | IP | Role |
|--------|----|------|
| [Cradlepoint IBR600](devices/cradlepoint-ibr600.md) | TBD | LTE WAN uplink, remote access gateway |
| [Ubiquiti USW-Lite-8-PoE](devices/ubiquiti-usw-lite-8-poe.md) | TBD | Layer 2 managed switch |
| [Weidian Mini PC](devices/weidian-mini-pc.md) | TBD | Linux tooling and logging host |

The IBR600 provides LTE connectivity managed via NetCloud Manager, enabling remote SSH/VPN access without a fixed IP. The USW-Lite-8-PoE connects development devices and provides a cross-connect uplink into the EMA assembly.

---

### Energy Management Assembly

| Device | IP | Role |
|--------|----|------|
| [Cradlepoint S700](devices/cradlepoint-s700.md) | TBD | LTE WAN uplink |
| [Ubiquiti USW-Pro-8-PoE 120W](devices/ubiquiti-usw-pro-8-poe.md) | TBD | Core managed PoE switch |
| [Phoenix Contact PC](devices/phoenix-contact-pc.md) | TBD | Industrial controller / automation host |

The EMA assembly is a self-contained unit on the gold-plate panel simulating a field-deployed energy management system. It has an independent LTE uplink (S700) separate from the development environment.

---

### Target Hardware

| Device | IP | Protocols |
|--------|-----|-----------|
| [SEL RTAC 3505](devices/sel-rtac-3505.md) | TBD | DNP3, Modbus TCP/RTU, IEC 61850, SEL protocol |
| [eGauge 4015](devices/egauge-4015.md) | TBD | Modbus TCP, HTTP REST API |

---

## Physical Topology

```
[Internet / LTE]
      |                    |
  [IBR600]             [S700]
      |                    |
  [USW-Lite] --------- [USW-Pro]
      |                /   |    \
  [Weidian]      [PHX PC] [RTAC] [eGauge]
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
