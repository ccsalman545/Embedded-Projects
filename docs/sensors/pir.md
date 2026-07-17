# PIR motion sensor HC-SR501

![Conceptual PIR motion sensor HC-SR501 pin reference](../../assets/illustrations/sensors/pir.svg)

> **Quick decision:** choose this for **human/animal motion, not presence**. It communicates over **Digital threshold** and typical Indian retail pricing is **₹80–180** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Digital threshold |
| Supply | 4.5–20 V |
| Typical price in India | ₹80–180 |
| Same-job alternative | mmWave radar / microwave Doppler |
| Primary technique | Pyroelectric differential IR sensing with Fresnel lens |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `VCC` | power |
| `OUT` | logic motion output |
| `GND` | return |
| `sensitivity/time potentiometers on module` | See module documentation |

## How it works

Pyroelectric differential IR sensing with Fresnel lens. The module conditions or digitises that physical effect, then exposes it through Digital threshold. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Digital threshold]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** security light, occupancy trigger. It is a practical choice when human/animal motion, not presence; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Digital threshold recipe](../PROGRAM_COOKBOOK.md#digital-threshold). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **PIR motion sensor HC-SR501** | human/animal motion, not presence | Verify calibration, operating range and module variant |
| **mmWave radar / microwave Doppler** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for security light, occupancy trigger.
- Digital threshold can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [www.mpja.com](https://www.mpja.com/download/31227sc.pdf)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
