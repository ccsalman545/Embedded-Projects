# SHT31 temperature & humidity

![Conceptual SHT31 temperature & humidity pin reference](../../assets/illustrations/sensors/sht31.svg)

> **Quick decision:** choose this for **repeatable environmental measurements**. It communicates over **I²C** and typical Indian retail pricing is **₹450–850** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | I²C |
| Supply | 2.4–5.5 V |
| Typical price in India | ₹450–850 |
| Same-job alternative | BME280 / AHT20 |
| Primary technique | Digital capacitive humidity sensor with band-gap temperature sensor |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `VIN` | power |
| `GND` | return |
| `SDA` | I²C data |
| `SCL` | I²C clock |
| `ADR` | address select |

## How it works

Digital capacitive humidity sensor with band-gap temperature sensor. The module conditions or digitises that physical effect, then exposes it through I²C. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[I²C]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** HVAC, weather station, museum logger. It is a practical choice when repeatable environmental measurements; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the I²C recipe](../PROGRAM_COOKBOOK.md#i2c). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **SHT31 temperature & humidity** | repeatable environmental measurements | Verify calibration, operating range and module variant |
| **BME280 / AHT20** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for HVAC, weather station, museum logger.
- I²C can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [sensirion.com](https://sensirion.com/products/catalog/SHT31-DIS)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
