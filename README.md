# Embedded Projects — Sensor & Board Reference Library

A practical, structured reference collection for embedded-system enthusiasts: **50 sensors** and **10 development boards**, with common pin functions, conceptual pin illustrations, operating techniques, Mermaid block diagrams, applications, INR price ranges, alternatives, trade-offs and firmware bring-up paths.

> **Start here:** [Sensor catalogue](docs/SENSOR_CATALOG.md) · [Board catalogue](docs/BOARD_CATALOG.md) · [Program cookbook](docs/PROGRAM_COOKBOOK.md) · [Verification & safety policy](docs/REFERENCE_POLICY.md)

## What every entry provides

- Common module/breakout pins and their use (always verify your board silk screen)
- An original, accessible SVG reference illustration and a signal block diagram
- Physical sensing technique, applications and selection rationale
- Indicative India price range as of **17 July 2026**
- Comparison with a same-function alternative, plus advantages and limitations
- Two applicable program paths with expected output and what that output can—and cannot—infer
- Primary manufacturer or official documentation link

## Fast, safe workflow

1. Select a sensor by interface and measurement goal in the [catalogue](docs/SENSOR_CATALOG.md).
2. Read its **pins**, **limitations**, comparison and linked primary datasheet.
3. Run its interface recipe from the [cookbook](docs/PROGRAM_COOKBOOK.md) before adding application logic.
4. Calibrate against a suitable reference, document conditions, then use filtered telemetry/control.

## Important boundary

This is an educational hardware reference, not a substitute for a current datasheet, exact module schematic or safety certification. In particular, low-cost gas, flame, health, mains-current and motion modules must not be the sole basis of a safety- or medical-critical decision. See the [reference policy](docs/REFERENCE_POLICY.md).

## Maintain the catalogue

The source records and generator are in `tools/build_catalog.py`. After changing records, run:

```bash
python3 tools/build_catalog.py
```

This regenerates the individual entry pages, index tables and original SVG illustrations consistently.

## License

MIT
