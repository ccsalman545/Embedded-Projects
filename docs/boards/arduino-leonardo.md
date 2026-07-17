# Arduino Leonardo

![Conceptual Arduino Leonardo board pin reference](../../assets/illustrations/boards/arduino-leonardo.svg)

> **Role:** native USB HID (keyboard/mouse) and 5 V Arduino projects. Typical Indian retail range: **₹900–2,000** (indicative on 17 July 2026, not a live quote).

| Property | Reference |
|---|---|
| Controller | ATmega32U4, 16 MHz, 5 V |
| I/O summary | 20 digital I/O (7 PWM), 12 analog inputs, native USB |
| Logic level | Check the board documentation; many pins are 3.3 V-only |
| Alternative | Arduino Uno / Micro |

## Reference pinout — key pins and connectors

> These labels and functions are for the named reference board revision. Header position and alternate functions must be checked against the official board pinout linked below; do not transfer Arduino-style labels between different board families.

| Pin / connector | Use |
|---|---|
| `Micro-USB` | power/programming |
| `D0/RX,D1/TX` | UART |
| `D2/SDA,D3/SCL` | I²C |
| `ICSP` | SPI |
| `VIN/5V/3V3/GND` | rails |

```mermaid
flowchart LR
  USB[USB / power] --> MCU[Microcontroller board]
  MCU --> GPIO[GPIO / ADC / PWM]
  MCU --> Buses[I²C · SPI · UART]
  Buses --> Sensors[Sensors & modules]
  GPIO --> Actuators[Drivers & actuators]
```

## Applications, technique and selection

The board executes firmware stored in its controller and uses digital/analog peripherals to sample sensors and drive outputs. Choose it for **native USB HID (keyboard/mouse) and 5 V Arduino projects**: its processor, voltage domain, memory, connectivity and physical size determine whether it fits. Typical applications include data loggers, control panels, robotics and connected sensor nodes.

## Three first programs, output and inference

1. [Blink / GPIO smoke test](../PROGRAM_COOKBOOK.md#blink-gpio-smoke-test): LED changes every second — proves upload, clock and output pin.
2. [I²C scanner](../PROGRAM_COOKBOOK.md#i2c-scanner): serial output lists responding addresses — proves shared-bus wiring.
3. [Filtered telemetry and alarm](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm): serial readings and state — proves the acquisition-to-decision loop.

**Inference:** passing these tests does not establish voltage compatibility or sensor accuracy. Confirm common ground, logic levels, current budget and exact pin multiplexing before expansion.

## Comparison and trade-offs

| Board | Best when | Trade-off |
|---|---|---|
| **Arduino Leonardo** | native USB HID (keyboard/mouse) and 5 V Arduino projects | Check its exact variant, USB interface and voltage limits |
| **Arduino Uno / Micro** | requirements differ in wireless capability, speed, I/O or power | requires a different toolchain or wiring plan |

**Advantages:** popular tools/tutorials; flexible interfaces; fast iteration.

**Disadvantages:** development boards are not automatically rugged, low-power or electrically protected products; add regulator, protection, enclosure and driver circuitry where needed.

## Verification source

- Official documentation: [docs.arduino.cc](https://docs.arduino.cc/hardware/leonardo/)
- [Reference policy](../REFERENCE_POLICY.md)
