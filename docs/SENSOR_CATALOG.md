# Sensor catalogue

**55 documented sensors** · pin use · conceptual pin images · block diagrams · applications · INR range · techniques · comparisons · advantages/limits · two tested workflow paths per entry.

Prices are indicative Indian hobby-retail ranges on **17 July 2026**, not live listings. Read [Reference policy](REFERENCE_POLICY.md) before buying or wiring.

| Sensor | Interface | Choose it for | INR |
|---|---|---|---|
| [DHT11 temperature & humidity](sensors/dht11.md) | Single-wire digital | low-cost room climate indication | ₹70–140 |
| [DHT22 / AM2302](sensors/dht22.md) | Single-wire digital | better range and accuracy than DHT11 | ₹220–450 |
| [SHT31 temperature & humidity](sensors/sht31.md) | I²C | repeatable environmental measurements | ₹450–850 |
| [BME280 environmental](sensors/bme280.md) | I²C / SPI | temperature, RH and barometric pressure in one part | ₹280–650 |
| [BMP280 barometric pressure](sensors/bmp280.md) | I²C / SPI | pressure and relative altitude trend | ₹180–450 |
| [DS18B20 waterproof temperature](sensors/ds18b20.md) | 1-Wire | robust, addressable temperature probes | ₹120–260 |
| [LM35 analog temperature](sensors/lm35.md) | Analog voltage | simple calibrated analog temperature | ₹45–120 |
| [TMP36 analog temperature](sensors/tmp36.md) | Analog voltage | low-voltage analog thermal measurement | ₹80–180 |
| [NTC thermistor module](sensors/ntc-thermistor.md) | Analog voltage | fast, inexpensive thermal thresholding | ₹40–100 |
| [MQ-2 smoke / LPG gas](sensors/mq2.md) | Analog + digital threshold | low-cost combustible-gas alarm experiments | ₹90–180 |
| [MQ-135 air-quality gas](sensors/mq135.md) | Analog + digital threshold | qualitative ventilation/air-change indicator | ₹100–220 |
| [PMS5003 particulate matter](sensors/pms5003.md) | UART | PM1/PM2.5/PM10 mass-concentration estimate | ₹1,500–3,000 |
| [BH1750 ambient light](sensors/bh1750.md) | I²C | ambient illuminance in lux | ₹100–250 |
| [LDR photoresistor module](sensors/ldr.md) | Analog + digital threshold | very low-cost light/dark detection | ₹30–80 |
| [HC-SR04 ultrasonic distance](sensors/hc-sr04.md) | Pulse timing | non-contact distance over a short range | ₹70–150 |
| [VL53L0X laser ToF distance](sensors/vl53l0x.md) | I²C | compact optical distance measurement | ₹500–1,000 |
| [Sharp GP2Y0A21 IR distance](sensors/gp2y0a21.md) | Analog voltage | short-range distance with simple ADC | ₹700–1,400 |
| [PIR motion sensor HC-SR501](sensors/pir.md) | Digital threshold | human/animal motion, not presence | ₹80–180 |
| [RCWL-0516 microwave motion](sensors/rcwl0516.md) | Digital threshold | motion detection through some non-metallic covers | ₹70–180 |
| [Reed switch magnetic door sensor](sensors/reed-switch.md) | Digital contact | reliable open/close state | ₹25–100 |
| [A3144 Hall-effect sensor](sensors/a3144.md) | Digital open collector | contactless magnet detection | ₹40–120 |
| [AS5600 magnetic encoder](sensors/as5600.md) | I²C / analog / PWM | absolute rotary position | ₹300–750 |
| [MPU6050 IMU](sensors/mpu6050.md) | I²C | linear acceleration and angular-rate sensing | ₹180–450 |
| [ADXL345 accelerometer](sensors/adxl345.md) | I²C / SPI | low-power acceleration, tap and free-fall events | ₹250–650 |
| [LIS3DH accelerometer](sensors/lis3dh.md) | I²C / SPI | low-power motion and orientation events | ₹250–650 |
| [QMC5883L magnetometer](sensors/qmc5883l.md) | I²C | low-cost compass heading after calibration | ₹120–320 |
| [NEO-6M GPS receiver](sensors/neo6m.md) | UART | position, speed and UTC time outdoors | ₹650–1,400 |
| [MAX30102 pulse-oximeter](sensors/max30102.md) | I²C | educational heart-rate / SpO₂ estimation—not diagnostic | ₹250–650 |
| [Soil moisture probe](sensors/soil-moisture.md) | Analog + digital threshold | rough soil wet/dry indication; corrodes if powered continuously | ₹50–130 |
| [Capacitive soil moisture sensor](sensors/capacitive-soil.md) | Analog voltage | less-corrosive soil moisture trend | ₹120–280 |
| [Rain / raindrop module](sensors/rain.md) | Analog + digital threshold | detect rain/water presence; plate corrodes | ₹60–150 |
| [Water level float switch](sensors/float-switch.md) | Digital contact | simple point-level detection | ₹60–180 |
| [Turbidity sensor SEN0189](sensors/turbidity.md) | Analog voltage | relative water clarity; calibrate with standards | ₹750–1,600 |
| [TDS / conductivity module](sensors/tds.md) | Analog voltage | water conductivity/TDS trend with temperature compensation | ₹650–1,500 |
| [pH electrode interface](sensors/ph.md) | Analog voltage | pH after two/three-point calibration | ₹1,200–3,000 |
| [HX711 load-cell ADC](sensors/hx711.md) | Two-wire synchronous | weight/force after tare and calibration | ₹120–300 (ADC); load cell extra |
| [Load cell strain gauge](sensors/load-cell.md) | Bridge analog (via HX711) | force or mass with stable mechanics and calibration | ₹300–1,500 |
| [FSR force-sensitive resistor](sensors/fsr.md) | Analog voltage | qualitative touch/force detection, not precision weighing | ₹250–700 |
| [Flex sensor](sensors/flex-sensor.md) | Analog voltage | bend-angle proxy after per-device calibration | ₹500–1,200 |
| [Sound sensor MAX9814](sensors/max9814.md) | Analog voltage | audio amplitude/envelope—not calibrated dB without calibration | ₹220–550 |
| [INMP441 I²S microphone](sensors/inmp441.md) | I²S digital audio | digital audio capture with known sample format | ₹250–650 |
| [Flame sensor module](sensors/flame.md) | Analog + digital threshold | flame indication in controlled demos; not fire-safety certified | ₹70–170 |
| [TCS34725 colour sensor](sensors/tcs34725.md) | I²C | colour classification under controlled illumination | ₹550–1,100 |
| [INA219 current / voltage](sensors/ina219.md) | I²C | bus voltage, current and power after calibration | ₹220–550 |
| [ACS712 current sensor](sensors/acs712.md) | Analog voltage | AC/DC current waveform or level; calibrate zero offset | ₹180–450 |
| [MAX6675 K-type thermocouple](sensors/max6675.md) | SPI-like | high-temperature K-type measurement | ₹250–650 |
| [MLX90614 IR thermometer](sensors/mlx90614.md) | I²C / SMBus | non-contact surface temperature; emissivity matters | ₹900–2,000 |
| [FC-51 IR obstacle sensor](sensors/fc51-ir-obstacle.md) | Digital threshold | simple short-range obstacle indication | ₹40–100 |
| [TTP223 capacitive touch sensor](sensors/ttp223-touch.md) | Digital threshold | a sealed, no-moving-parts touch switch | ₹40–100 |
| [RC522 RFID / NFC reader](sensors/rc522-rfid.md) | SPI | low-cost local tag identification | ₹120–300 |
| [YF-S201 water-flow sensor](sensors/yf-s201-flow.md) | Pulse timing | inexpensive water-flow totalisation after calibration | ₹250–600 |
| [SW-420 vibration sensor](sensors/sw420-vibration.md) | Analog + digital threshold | simple impact or vibration event indication | ₹40–100 |
| [KY-033 line-tracking sensor](sensors/ky033-line-tracker.md) | Analog + digital threshold | high-contrast line detection near the surface | ₹50–130 |
| [VS1838B IR remote receiver](sensors/vs1838b-ir.md) | Digital pulse | decode common consumer IR remotes | ₹60–160 |
| [MQ-3 alcohol gas sensor](sensors/mq3.md) | Analog + digital threshold | educational alcohol-vapour trend experiments | ₹100–250 |

## Browse by signal

- **Analog:** LM35, TMP36, NTC, MQ modules, LDR, distance IR, soil/rain/turbidity/TDS/pH, force/flex, microphone, INA/ACS and thermocouple interfaces.
- **I²C/SPI:** environmental, light, ToF, IMU, magnetometer, optical, current and IR-temperature devices.
- **Digital/timing:** DHT, DS18B20, ultrasonic, motion, reed/Hall and float switches.
- **UART:** particulate sensors and GPS.

For initial firmware and expected results, use the [Program cookbook](PROGRAM_COOKBOOK.md).
