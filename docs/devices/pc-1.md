# PC-1 — Fanless PC

<!-- NETJSON:START -->
| Field | Value |
|-------|-------|
| **Tag** | PC-1 |
| **Manufacturer** | Weidian |
| **Model** | TBD |
| **Type** | Industrial Fanless Mini PC |
| **Subsystem** | Development Subsystem |
| **Hostname** | chad-lab1913 |
| **IP Address** | 172.22.1.40, 10.0.0.103 |
| **MAC Address** | 8c:03:60:4c:d5:fa |
| **Serial Number** | TBD |
| **Management** | SSH |
| **Management URL** | ssh chad@172.22.1.40 |
<!-- NETJSON:END -->

## Role

General-purpose Linux environment for tooling development and log aggregation. Serves as the primary workstation on the lab bench for:

- Writing and testing protocol scripts (Modbus, DNP3, etc.)
- Running log collection and aggregation agents
- Development of observability tooling
- Ad-hoc device testing and commissioning

## Key Specs

- **CPU:** Intel Core i7-10810U @ 1.10GHz (6 cores / 12 threads)
- **RAM:** 32 GB
- **Storage:** 915 GB NVMe (WD Green SN350 1TB) — 27 GB used
- **OS:** Ubuntu 24.04.2 LTS (Noble Numbat)
- Fanless industrial form factor
- 2x GbE Ethernet ports + WiFi
- USB and serial interfaces

## Interfaces

<!-- NETJSON:INTERFACES:START -->
| Interface | Type | Role | Address | Notes |
|-----------|------|------|---------|-------|
| enp1s0 | ethernet | lan | 172.22.1.40/24 | NS-1 P2 — primary lab network |
| enp2s0 | ethernet | lan | TBD | spare, unplugged |
| wlp3s0 | wifi | mgmt | 10.0.0.103/24 | home network WiFi — DHCP, backup access |
<!-- NETJSON:INTERFACES:END -->

## Physical Connections

- **enp1s0:** → NS-1 (USW-Lite-8-PoE) Port P2 (connected, 172.22.1.40)
- **enp2s0:** spare, unplugged
- **wlp3s0:** WiFi, home network (10.0.0.103, secondary/backup access)

## Installed Software

| Tool | Purpose |
|------|---------|
| Docker | Container runtime (docker0 bridge at 172.17.0.1) |
| SSH server | Remote management |
| unifi_controller | UniFi Network controller (jacobalberty/unifi:latest) — manages lab switches/APs |
| unifi_mongo | MongoDB 3.6 — UniFi controller database (internal only, port 27017) |
| unifi_logs | Log sidecar for UniFi |

## Services

| Service | URL | Notes |
|---------|-----|-------|
| UniFi Controller | https://10.0.0.103:8443 or https://172.22.1.40:8443 | Self-signed cert; manages all lab network gear |

## Management Access

- **SSH:** `ssh chad@172.22.1.40` (lab network) or `ssh chad@10.0.0.103` (WiFi DHCP — may change)
- **Console:** HDMI + USB keyboard; BIOS boot override via F10 → Boot Override

## Notes

- WiFi IP (10.0.0.103) is DHCP-assigned — consider setting a DHCP reservation for stable backup access
- enp1s0 also has a secondary address 192.168.0.40/24 — origin unknown, investigate and clean up
- **HDMI display fix (resolved):** eDP-1 connector falsely reported as connected, causing GDM3 to render the login screen on a non-existent internal display. Fixed by: (1) disabling Wayland (`/etc/gdm3/custom.conf` → `WaylandEnable=false`), (2) allowing Xorg for all users (`/etc/X11/Xwrapper.config` → `allowed_users=anybody`), (3) creating `/etc/X11/xorg.conf.d/10-display.conf` to ignore eDP-1 and set HDMI-1 as primary. Workaround if needed: `Ctrl+Alt+F2` for TTY, then `sudo -u gdm DISPLAY=:0 XAUTHORITY=/run/user/120/gdm/Xauthority xrandr --output eDP-1 --off --output HDMI-1 --primary --auto`.
- SGX disabled/unsupported per BIOS (non-critical kernel message on boot)
- NS-1 adoption fix: if switch shows "Adopting/Unreachable", SSH to switch (`ssh ubnt@172.22.1.3`) and run `set-inform http://172.22.1.40:8080/inform` twice — switch will reboot and connect
