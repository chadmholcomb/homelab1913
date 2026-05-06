# NS-1 — Ubiquiti USW-Lite-8-PoE

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | NS-1 |
| **Manufacturer** | Ubiquiti |
| **Model** | USW-Lite-8-PoE |
| **Type** | Managed Layer 2 PoE Switch |
| **Segment** | Development Environment |
| **Hostname** | TBD |
| **IP Address** | 172.22.1.3 |
| **MAC Address** | 0C:EA:14:7F:BC:92 |
| **Serial Number** | TBD |
| **Management** | UniFi Network Controller |
| **Management URL** | https://10.0.0.103:8443 |
<!-- NETJSON:END -->

## Role

Core switch for the development environment. Connects all development-side devices and provides the cross-connect uplink into the Energy Management Assembly at NS-2.

## Key Specs

- 8x GbE ports total
- Ports 1–4: PoE+ (IEEE 802.3af/at), 52W total budget
- Ports 5–8: non-PoE
- Managed via UniFi Network Controller
- Fanless, wall/desktop mountable

## Port Map

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| P1 | ethernet | uplink | TBD | MOD-1 LAN |
| P2 | ethernet | access | 172.22.1.40 | PC-1 (enp1s0) |
| P3 | ethernet | access | TBD | TBD |
| P4 | ethernet | access | TBD | TBD |
| P5 | ethernet | access | TBD | TBD |
| P6 | ethernet | access | TBD | TBD |
| P7 | ethernet | access | TBD | TBD |
| P8 | ethernet | trunk | TBD | Cross-connect to NS-2 P1 |
<!-- NETJSON:INTERFACES:END -->

## Management Access

- **UniFi Controller:** https://10.0.0.103:8443 (running on PC-1)
- **SSH:** `ssh ubnt@172.22.1.3` (default credentials)
- **Firmware:** 6.4.19

## VLANs

| VLAN | Name | Subnet | Gateway | Ports |
|------|------|--------|---------|-------|
| 2 | lan (Primary LAN) | 172.22.1.0/24 | 172.22.1.1 (MOD-1) | 1U, 2U |
| 168 | AUX | 192.168.168.0/24 | 192.168.168.1 | 1T |
| 20 | GUEST | 192.168.20.0/24 | 192.168.20.1 | 1T |

## Notes

- Primary LAN routed via Cradlepoint IBR600 (MOD-1) at 172.22.1.1
- AUX VLAN serves WiFi AP POWERFLEX-DMZ (2.4 GHz)
- GUEST VLAN serves WiFi AP Public-fc5 (2.4 GHz)
- UniFi controller hosted on PC-1 Docker container
