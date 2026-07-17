# ADXL345 accelerometer

![Conceptual ADXL345 accelerometer pin reference](../../assets/illustrations/sensors/adxl345.svg)

> **Quick decision:** choose this for **low-power acceleration, tap and free-fall events**. It communicates over **I²C / SPI** and typical Indian retail pricing is **₹250–650** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | I²C / SPI |
| Supply | 1.8–3.6 V |
| Typical price in India | ₹250–650 |
| Same-job alternative | MPU6050 / LIS3DH |
| Primary technique | MEMS capacitive 3-axis acceleration |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `VCC` | power |
| `GND` | return |
| `SDA/SDI` | data |
| `SCL/SCLK` | clock |
| `CS` | select |
| `SDO` | address/MISO |
| `INT1/2` | interrupts |

## How it works

MEMS capacitive 3-axis acceleration. The module conditions or digitises that physical effect, then exposes it through I²C / SPI. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[I²C / SPI]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** activity tracker, impact logger, tilt switch. It is a practical choice when low-power acceleration, tap and free-fall events; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the I²C / SPI recipe](../PROGRAM_COOKBOOK.md#i2c). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **ADXL345 accelerometer** | low-power acceleration, tap and free-fall events | Verify calibration, operating range and module variant |
| **MPU6050 / LIS3DH** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for activity tracker, impact logger, tilt switch.
- I²C / SPI can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [www.analog.com](https://www.analog.com/en/products/adxl345.html)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
