# SGP30 eCO₂ / TVOC

![Conceptual SGP30 eCO₂ / TVOC pin reference](../../assets/illustrations/sensors/sgp30.svg)

> **Quick decision:** choose this for **compact air-quality trend**. It communicates over **I²C** and typical Indian retail pricing is **₹800–1,600** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | I²C |
| Supply | 1.62–1.98 V core; breakout regulated |
| Typical price in India | ₹800–1,600 |
| Same-job alternative | CCS811 / ENS160 |
| Primary technique | MOx gas pixels with humidity-compensated IAQ algorithm |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `VIN` | breakout power |
| `GND` | return |
| `SDA` | data |
| `SCL` | clock |

## How it works

MOx gas pixels with humidity-compensated IAQ algorithm. The module conditions or digitises that physical effect, then exposes it through I²C. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[I²C]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** smart home, purifier control. It is a practical choice when compact air-quality trend; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the I²C recipe](../PROGRAM_COOKBOOK.md#i2c). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **SGP30 eCO₂ / TVOC** | compact air-quality trend | Verify calibration, operating range and module variant |
| **CCS811 / ENS160** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for smart home, purifier control.
- I²C can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [sensirion.com](https://sensirion.com/products/catalog/SGP30)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
