# Arduino Due

![Conceptual Arduino Due board pin reference](../../assets/illustrations/boards/arduino-due.svg)

> **Role:** faster 3.3 V Arduino-class projects with DAC. Typical Indian retail range: **₹2,500–5,000** (indicative on 17 July 2026, not a live quote).

| Property | Reference |
|---|---|
| Controller | ATSAM3X8E Cortex-M3, 84 MHz, 3.3 V |
| I/O summary | 54 digital I/O (12 PWM), 12 analog inputs, 2 DAC |
| Logic level | Check the board documentation; many pins are 3.3 V-only |
| Alternative | Mega 2560 / STM32 |

## Reference pinout — key pins and connectors

> These labels and functions are for the named reference board revision. Header position and alternate functions must be checked against the official board pinout linked below; do not transfer Arduino-style labels between different board families.

| Pin / connector | Use |
|---|---|
| `Programming/Native USB` | upload |
| `D20/SDA,D21/SCL` | I²C |
| `ICSP` | SPI |
| `Serial0–3` | UARTs |
| `3V3/GND` | logic rails |
| `all GPIO are 3.3 V` | See board documentation |

```mermaid
flowchart LR
  USB[USB / power] --> MCU[Microcontroller board]
  MCU --> GPIO[GPIO / ADC / PWM]
  MCU --> Buses[I²C · SPI · UART]
  Buses --> Sensors[Sensors & modules]
  GPIO --> Actuators[Drivers & actuators]
```

## Applications, technique and selection

The board executes firmware stored in its controller and uses digital/analog peripherals to sample sensors and drive outputs. Choose it for **faster 3.3 V Arduino-class projects with DAC**: its processor, voltage domain, memory, connectivity and physical size determine whether it fits. Typical applications include data loggers, control panels, robotics and connected sensor nodes.

## Three first programs, output and inference

1. [Blink / GPIO smoke test](../PROGRAM_COOKBOOK.md#blink-gpio-smoke-test): LED changes every second — proves upload, clock and output pin.
2. [I²C scanner](../PROGRAM_COOKBOOK.md#i2c-scanner): serial output lists responding addresses — proves shared-bus wiring.
3. [Filtered telemetry and alarm](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm): serial readings and state — proves the acquisition-to-decision loop.

**Inference:** passing these tests does not establish voltage compatibility or sensor accuracy. Confirm common ground, logic levels, current budget and exact pin multiplexing before expansion.

## Comparison and trade-offs

| Board | Best when | Trade-off |
|---|---|---|
| **Arduino Due** | faster 3.3 V Arduino-class projects with DAC | Check its exact variant, USB interface and voltage limits |
| **Mega 2560 / STM32** | requirements differ in wireless capability, speed, I/O or power | requires a different toolchain or wiring plan |

**Advantages:** popular tools/tutorials; flexible interfaces; fast iteration.

**Disadvantages:** development boards are not automatically rugged, low-power or electrically protected products; add regulator, protection, enclosure and driver circuitry where needed.

## Verification source

- Official documentation: [docs.arduino.cc](https://docs.arduino.cc/hardware/due/)
- [Reference policy](../REFERENCE_POLICY.md)
