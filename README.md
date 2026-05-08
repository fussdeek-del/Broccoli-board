# Broccoli Board

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)]()
[![MCU](https://img.shields.io/badge/MCU-nice!nano%20V2-black?style=flat-square)]()
[![PCB](https://img.shields.io/badge/PCB-KiCad%2010-314CB0?style=flat-square)]()
[![Firmware](https://img.shields.io/badge/firmware-ZMK-00599C?style=flat-square)]()
[![Wireless](https://img.shields.io/badge/wireless-BLE%205.0-blueviolet?style=flat-square)]()

> A fully wireless 75% mechanical keyboard built from scratch custom PCB, per-key RGB, BLE 5.0, hot-swap switches, and a 3D printed case. Every component chosen, every trace routed by hand.

---

## What is it?

Broccoli Board is a custom 84-key 75% keyboard I designed completely from scratch. The PCB is designed in KiCad, the case in Fusion 360, and the firmware runs on ZMK. It's fully wireless over BLE 5.0 via the nice!nano V2, has per-key RGB LEDs reverse-mounted on the back of the PCB, and uses Kailh hot-swap sockets so I can swap switches without touching a soldering iron.

## Why i built it?
I didn't want to spend $200+ on a keyboard that still isn't fully mine. So I built one.

---

## Zine

![Zine](img%20assets/ZINE.png)

---

## Gallery

### CAD & Assembly
<table>
  <tr>
    <td><img src="img%20assets/full%20assembly%20CAD.jpg" width="400"/></td>
    <td><img src="img%20assets/side%20curved%20view.png" width="400"/></td>
  </tr>
</table>

### PCB
<table>
  <tr>
    <td><img src="img%20assets/PCB%20Fcu.png" width="400"/></td>
    <td><img src="img%20assets/PCB%20Bcu.png" width="400"/></td>
  </tr>
</table>
---

## Features

- 84 keys, 75% layout
- Wireless BLE 5.0 via nice!nano V2 (nRF52840)
- Per-key SK6812 Mini-E RGB reverse mount on B.Cu
- Kailh hot-swap sockets no soldering to swap switches
- Rotary encoder with push switch (EC11)
- USB-C wired + wireless dual mode
- 3.7V LiPo 2000mAh with MCP73831 charger IC
- 74AHCT125 level shifter for LED data
- USBLC6-2SC6 ESD protection on USB lines
- ZMK firmware
- 2-layer PCB, KiCad 10, JLCPCB fabrication
- Custom 3D printed case tray, plate, and bezel

---

## Hardware Specs

| Component | Details |
|---|---|
| MCU | nice!nano V2 (nRF52840), socketed |
| Layout | 75%, 84 keys |
| Switches | Gateron Blue × 84, 5-pin PCB mount |
| Hotswap | Kailh CPG151101S11 × 84 |
| LEDs | SK6812 Mini-E × 84, reverse mount |
| Encoder | EC11 rotary encoder with push switch |
| Wireless | Bluetooth 5.0 BLE |
| Firmware | ZMK |
| Battery | 3.7V LiPo 2000mAh (804050), JST PH2 |
| Charger IC | MCP73831, 500mA |
| Regulator | ME6211 3.3V LDO |
| Level shifter | 74AHCT125 |
| ESD protection | USBLC6-2SC6 |
| USB connector | GCT USB4105, 16-pin USB-C |
| PCB | 2-layer, JLCPCB, KiCad 10 |
| Case | SLA resin 3D print, Fusion 360 |
| Matrix | 9 rows × 10 columns, col2row |

---

## How to Build

### Order the PCB
1. Go to [JLCPCB](https://jlcpcb.com)
2. Upload `pcb/gerbers.zip`
3. 2-layer, FR-4, 1.6mm, HASL or ENIG
4. Minimum order 5 boards

### Flash the Firmware
1. Fork the [ZMK firmware repo](https://github.com/fussdeek-del/Broccoli--board-zmk)
2. Edit keymap at `boards/shields/broccoli_board/broccoli_board.keymap`
3. Push GitHub Actions builds automatically
4. Download `.uf2` from Actions artifacts
5. Double-tap reset on nice!nano to enter bootloader
6. Drag `.uf2` onto the USB drive that appears

note: The frimware isn't completely, i will complete it once this gets approved.

### Assembly Notes
- Solder LEDs on **B.Cu** reverse mount facing down
- Solder hotswap sockets on **F.Cu**
- Solder the nice!nano v2
- Battery connects via JST PH2 to J2

## BOM

> 💰 Estimated total: **~$174 USD** — can drop to **$120–$140** buying locally.

| Component | Spec | Qty | Price | Notes | Link |
|---|---|---|---|---|---|
| Microcontroller (MCU) | nice!nano V2 nRF52840 | ×1 | $5.00 | Clone — cheaper, slightly less reliable | [Buy](https://www.aliexpress.com/item/1005006271881076.html) |
| 74AHCT125 Level Shifter | TSSOP-14 | ×1 | $2.52 | Pack of 10 — LED data 3.3V→5V | [Buy](https://www.aliexpress.com/item/1005008171122183.html) |
| MCP73831 LiPo Charger | SOT-23-5 | ×1 | $2.50 | Pack of 10 — LiPo charging IC | [Buy](https://www.aliexpress.com/item/1005007439657191.html) |
| ME6211 3.3V LDO | ME6211C33 SOT-23-5 | ×1 | $2.20 | Pack of 10 — 3.3V regulator | [Buy](https://www.aliexpress.com/item/1005007315116858.html) |
| USBLC6-2SC6 ESD Protection | SOT-23-6 | ×1 | $1.50 | Pack of 10 — USB ESD protection | [Buy](https://www.aliexpress.com/item/32807108222.html) |
| Gateron Blue Switch | G Pro Blue 5-pin | ×84 | $24.00 | Pack of 100 — 5-pin PCB mount | [Buy](https://www.aliexpress.com/item/1005006091988869.html) |
| Kailh Hotswap Socket | MX compatible | ×84 | $7.00 | Pack of 100 | [Buy](https://www.aliexpress.com/item/1005006105603269.html) |
| EC11 Rotary Encoder | 20mm with push switch | ×1 | $2.00 | Pack of 5 | [Buy](https://www.aliexpress.com/item/1005006460161288.html) |
| Reset Button | SMD tactile 3×4mm | ×1 | $1.50 | Pack of 30 | [Buy](https://www.aliexpress.com/item/4001107416458.html) |
| SK6812 Mini-E RGB LED | Reverse mount | ×84 | $13.50 | Pack of 100 — buy 100, need 84 + spares | [Buy](https://www.aliexpress.com/item/1005004249903121.html) |
| 1N4148W Matrix Diode | SOD-123 | ×84 | $1.50 | Pack of 100 — buy 100, need 84 + spares | [Buy](https://www.aliexpress.com/item/1005010728396328.html) |
| Resistor 10K | 0603 | ×10 | $1.20 | Pack of 300 | [Buy](https://www.aliexpress.com/item/1005011779883974.html) |
| Resistor 5.1K | 0603 | ×5 | $1.30 | Pack of 300 | [Buy](https://www.aliexpress.com/item/1005011779883974.html) |
| Resistor 330Ω | 0603 | ×1 | $2.00 | Pack of 500 | [Buy](https://www.aliexpress.com/item/1005005700395390.html) |
| Capacitor 100nF | 0805 | ×100 | $2.00 | Pack of 200 | [Buy](https://www.aliexpress.com/item/1005007660078779.html) |
| Capacitor 10µF | 0805 | ×1 | $2.20 | Pack of 200 | [Buy](https://www.aliexpress.com/item/1005007660078779.html) |
| USB-C Receptacle 16P | GCT USB4105 SMD | ×1 | $4.50 | Pack of 5 | [Buy](https://www.aliexpress.com/item/1005005581945089.html) |
| JST PH2 2-pin | PH2.0 2-pin connector | ×1 | $2.00 | Pack of 2 | [Buy](https://www.aliexpress.com/item/1005010615395743.html) |
| Polyfuse 500mA | Resettable fuse 1206 | ×1 | $1.70 | Pack of 10 | [Buy](https://www.aliexpress.com/item/1005005235906949.html) |
| LiPo 3.7V 2000mAh | 804050, JST PH | ×1 | $9.40 | Price for 2 | [Buy](https://www.aliexpress.com/item/1005005984841109.html) |
| Keycap Set | PBT 75% MX compatible | ×75 | $22.50 | 100+ keycaps included | [Buy](https://www.aliexpress.com/item/1005007416863215.html) |
| Rotary Knob | Aluminum 6mm D shaft 20mm | ×1 | $2.00 | 2 pieces | [Buy](https://www.aliexpress.com/item/4001091267351.html) |
| PCB Fabrication | 2-layer, FR-4, 1.6mm, HASL | ×5 boards | $22.20 | Minimum 5 pieces | [JLCPCB](https://cart.jlcpcb.com/quote) |
| 3D Print — Tray | SLA resin | ×1 | $25.30 | Local 3D printer recommended | [JLC3DP](https://jlc3dp.com/3d-printing-quote) |
| 3D Print — Top Plate | SLA resin | ×1 | $8.30 | Local 3D printer recommended | [JLC3DP](https://jlc3dp.com/3d-printing-quote) |
| 3D Print — Top Cover | SLA resin | ×1 | $2.65 | Local 3D printer recommended | [JLC3DP](https://jlc3dp.com/3d-printing-quote) |
| M3 Screws | M3 × 8mm countersunk | ×10 | $1.00 | Pack of 50 | [Buy](https://www.aliexpress.com/item/1005008810897680.html) |
| M3 Standoffs | M3 × 4mm | ×10 | $1.00 | Pack of 50 | [Buy](https://www.aliexpress.com/item/1005008810897680.html) |

---
## Schematics note
Schematics is reviewed my multiple people in fallout + AI. there was problem init that i fixed, and now it LGTM
repo is surface checked by riitam
## Credits

- [KiCad](https://www.kicad.org/) — PCB design
- [ZMK Firmware](https://zmk.dev/) — open source keyboard firmware
- [Fusion 360](https://www.autodesk.com/products/fusion-360/) — case design
- [nice!nano](https://nicekeyboards.com/nice-nano/) — nRF52840 BLE module
- [Hack Club Fallout](https://fallout.hackclub.com) — grant that made this real

Made by **Nabeel Ahmed (18) × Hashir (17)** — Punjab, Pakistan 🇵🇰

---

## License

MIT
