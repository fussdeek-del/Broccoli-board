# Broccoli Board

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)]()
[![MCU](https://img.shields.io/badge/MCU-nice!nano%20V2-black?style=flat-square)]()
[![PCB](https://img.shields.io/badge/PCB-KiCad%2010-314CB0?style=flat-square)]()
[![Firmware](https://img.shields.io/badge/firmware-ZMK-00599C?style=flat-square)]()
[![Wireless](https://img.shields.io/badge/wireless-BLE%205.0-blueviolet?style=flat-square)]()

> A fully wireless 75% mechanical keyboard built from scratch — custom PCB, per-key RGB, BLE 5.0, hot-swap switches, and a 3D printed case. Every component chosen, every trace routed by hand.

![Zine Page](img%20assets/ZINE.png)

---

## What is it?

Broccoli Board is a custom 84-key 75% keyboard I designed completely from scratch. The PCB is designed in KiCad, the case in Fusion 360, and the firmware runs on ZMK. It's fully wireless over BLE 5.0 via the nice!nano V2, has per-key RGB LEDs reverse-mounted on the back of the PCB, and uses Kailh hot-swap sockets so I can swap switches without touching a soldering iron.

I didn't want to spend $200+ on a keyboard that still isn't fully mine. So I built one.

---

## Demo

![Full assembly](img%20assets/full-assembly.png)

![PCB layout](img%20assets/pcb.png)

![Schematic](img%20assets/schematic.png)

---

## Features

- 84 keys, 75% layout
- Wireless BLE 5.0 via nice!nano V2 (nRF52840)
- Per-key SK6812 Mini-E RGB — reverse mount on B.Cu
- Kailh hot-swap sockets — no soldering to swap switches
- Rotary encoder with push switch (EC11)
- USB-C wired + wireless dual mode
- 3.7V LiPo 2000mAh with MCP73831 charger IC
- 74AHCT125 level shifter for LED data
- USBLC6-2SC6 ESD protection on USB lines
- ZMK firmware
- 2-layer PCB, KiCad 10, JLCPCB fabrication
- Custom 3D printed case — tray, plate, and bezel

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
3. Push — GitHub Actions builds automatically
4. Download `.uf2` from Actions artifacts
5. Double-tap reset on nice!nano to enter bootloader
6. Drag `.uf2` onto the USB drive that appears

### Assembly Notes
- Solder LEDs on **B.Cu** reverse mount facing down
- Solder hotswap sockets on **F.Cu**
- Socket the nice!nano with mill-max sockets, don't solder directly
- Battery connects via JST PH2 to J2

---

## Repo Structure

    Broccoli-board/
    ├── README.md
    ├── Broccoli board BOM.csv
    ├── pcb/                 ← KiCad source files + gerbers.zip
    ├── cad/                 ← Fusion 360 + STEP exports
    ├── firmware/            ← ZMK shield files + build.yaml
    └── img assets/          ← screenshots and renders

> ZMK firmware repo: [Broccoli--board-zmk](https://github.com/fussdeek-del/Broccoli--board-zmk)

---

## BOM

[![BOM](https://img.shields.io/badge/BOM-CSV-green?style=flat-square)](./Broccoli%20board%20BOM.csv)

Full bill of materials with AliExpress and JLCPCB links — [view BOM file](./Broccoli%20board%20BOM.csv)

Estimated total: **~$153 USD** with clone nice!nano, **~$165 USD** with original.

---

## Credits

- [KiCad](https://www.kicad.org/) — PCB design
- [ZMK Firmware](https://zmk.dev/) — open source keyboard firmware
- [Fusion 360](https://www.autodesk.com/products/fusion-360/) — case design
- [nice!nano](https://nicekeyboards.com/nice-nano/) — nRF52840 BLE module
- [Hack Club Fallout](https://fallout.hackclub.com) — grant that made this real

Made by **broccoli Nabeel Ahmed(18) X Hashir(17),** — Punjab, Pakistan 🇵🇰

---

## License

MIT
