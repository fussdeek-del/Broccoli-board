# Broccoli Board

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)]()
[![MCU](https://img.shields.io/badge/MCU-nice!nano%20V2-black?style=flat-square)]()
[![PCB](https://img.shields.io/badge/PCB-KiCad%2010-314CB0?style=flat-square)]()
[![Firmware](https://img.shields.io/badge/firmware-ZMK-00599C?style=flat-square)]()
[![Wireless](https://img.shields.io/badge/wireless-BLE%205.0-blueviolet?style=flat-square)]()

> A fully wireless 75% custom mechanical keyboard with per-key RGB, hot-swap switches, rotary encoder, and a jet-black PCB — every component chosen, every trace routed by hand.

---

## What is it?

Broccoli Board is a custom 84-key 75% mechanical keyboard PCB built from scratch. It features full wireless BLE 5.0 via the nice!nano V2, per-key SK6812 Mini-E RGB LEDs in reverse mount, Kailh hot-swap sockets, a rotary encoder, and USB-C wired support. The entire case is custom-designed in Fusion 360 and 3D printed.

## Why I built it

Mechanical keyboards are expensive. The ones worth buying cost way more than I wanted to spend, and none of them felt fully mine. I wanted a keyboard where I chose every switch, every LED, every trace. So I designed one from scratch. Hack Club Fallout gave me the chance to actually build it for real — with a proper PCB, custom firmware, and a case I modeled myself.

---

## Demo

![Broccoli Board PCB](img%20assets/cover.png)

---

## Features

- 84 keys, 75% layout
- Wireless BLE 5.0 via nice!nano V2 (nRF52840)
- Per-key SK6812 Mini-E RGB LEDs — reverse mount on B.Cu
- Kailh hot-swap sockets — swap switches without soldering
- Rotary encoder with push switch (EC11)
- USB-C wired + wireless dual mode
- 3.7V LiPo 2000mAh battery with MCP73831 charger IC
- 74AHCT125 level shifter for LED data line
- USBLC6-2SC6 ESD protection on USB lines
- ZMK open-source firmware
- 2-layer PCB designed in KiCad 10
- Custom 3D printed case (Fusion 360)

---

## Hardware Specs

| Component | Details |
|---|---|
| MCU | nice!nano V2 (nRF52840), socketed |
| Layout | 75%, 84 keys |
| Switches | Gateron Blue × 84, 5-pin PCB mount |
| Hotswap | Kailh MX hotswap sockets × 84 |
| LEDs | SK6812 Mini-E × 84, reverse mount, per-key RGB |
| Encoder | EC11 rotary encoder with push switch |
| Wireless | Bluetooth 5.0 BLE |
| Firmware | ZMK |
| Battery | 3.7V LiPo 2000mAh (804050), JST PH2 |
| Charger | MCP73831, 500mA charge rate |
| Regulator | ME6211 3.3V LDO |
| Level shifter | 74AHCT125 (3.3V → 5V for LED data) |
| USB | USB-C receptacle, 16-pin (GCT USB4105) |
| PCB | 2-layer, JLCPCB, KiCad 10 |
| Case | 3D printed SLA resin, custom Fusion 360 |
| Matrix | 9 rows × 10 columns, col2row diodes |

---

## How to Build

### Order the PCB
1. Go to [JLCPCB](https://jlcpcb.com)
2. Upload `pcb/gerbers.zip`
3. Settings: 2-layer, FR-4, 1.6mm, HASL or ENIG finish
4. Minimum order is 5 boards

### Flash the Firmware
1. Fork the [ZMK firmware repo](https://github.com/fussdeek-del/Broccoli--board-zmk)
2. Modify keymap in `boards/shields/broccoli_board/broccoli_board.keymap`
3. Push to GitHub — firmware builds automatically via GitHub Actions
4. Download `.uf2` from Actions artifacts
5. Double-tap reset on nice!nano to enter bootloader
6. Drag `.uf2` onto the USB drive that appears

### Assembly Notes
- Solder LEDs on **B.Cu** (reverse mount, facing down)
- Solder hotswap sockets on **F.Cu**
- Socket the nice!nano using mill-max sockets
- JST PH2 connector for battery (J2)

---

## Repo Structure
'''
Broccoli-board/
├── README.md
├── Broccoli board BOM.csv
├── pcb/                        ← KiCad source + gerbers.zip
├── cad/                        ← Fusion 360 + STEP files
├── firmware/                   ← ZMK shield files + build.yaml
├── img assets/                 ← screenshots and renders
'''

> ZMK firmware repo: [Broccoli Board ZMK](https://github.com/fussdeek-del/Broccoli--board-zmk)

---

## BOM

Full bill of materials with links and prices: [`Broccoli board BOM.csv`](./Broccoli%20board%20BOM.csv)

Total estimated cost: **~$153 USD** (clone nice!nano) or **~$165 USD** (original)

---

## Zine Page

*Made for Hack Club Fallout — Shenzhen 2026*

![Broccoli Board Zine Page](img%20assets/zine.png)

---

## Credits

- [KiCad](https://www.kicad.org/) — PCB design
- [ZMK Firmware](https://zmk.dev/) — open source keyboard firmware
- [Fusion 360](https://www.autodesk.com/products/fusion-360/) — case design
- [nice!nano](https://nicekeyboards.com/nice-nano/) — nRF52840 BLE module
- [Hack Club Fallout](https://fallout.hackclub.com) — grant program that made this real

Made by **broccoli (Nabeel Ahmed), 18** — Pakistan 🇵🇰

---

## License

MIT
