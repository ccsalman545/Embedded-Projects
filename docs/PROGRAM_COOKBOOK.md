# Program cookbook: bring-up, output and inference

These diagnostic **Arduino-style** sketches establish wiring before application logic. Choose pins and ADC scaling for your board. Open Serial Monitor at 115200 baud unless noted.

## Blink GPIO smoke test

```cpp
const int LED=LED_BUILTIN;
void setup(){pinMode(LED,OUTPUT);}
void loop(){digitalWrite(LED,HIGH);delay(1000);digitalWrite(LED,LOW);delay(1000);}
```

**Output:** LED toggles each second. **Inference:** upload/clock/GPIO work; this does not validate a sensor.

## Analog voltage

For analog modules (temperature, gas, light, soil, water, force, sound, flame and current). Do not exceed the ADC reference voltage.

```cpp
const int PIN=A0;
void setup(){Serial.begin(115200);}
void loop(){int raw=analogRead(PIN); float v=raw*(5.0/1023.0); // Uno scale only
  Serial.print("raw=");Serial.print(raw);Serial.print(" V=");Serial.println(v,3);delay(500);}
```

**Output:** `raw=512 V=2.502`-like lines change with stimulus. **Inference:** ADC sees voltage, not automatically °C, ppm, pH, dB or force—apply transfer function and calibration.

## I2C

### I²C scanner

```cpp
#include <Wire.h>
void setup(){Wire.begin();Serial.begin(115200);for(byte a=8;a<120;a++){Wire.beginTransmission(a);if(Wire.endTransmission()==0){Serial.print("I2C @ 0x");Serial.println(a,HEX);}}}
void loop(){}
```

**Output:** e.g. `I2C @ 0x76`. **Inference:** SDA/SCL, pull-ups and an addressed device respond; it neither identifies the part nor proves valid measurements.

### I²C register skeleton

```cpp
#include <Wire.h>
const byte ADDRESS=0x76; // replace after scan
void setup(){Wire.begin();Serial.begin(115200);}
void loop(){Wire.beginTransmission(ADDRESS);Wire.write(0x00);if(Wire.endTransmission(false)){Serial.println("no ACK");}else{Wire.requestFrom(ADDRESS,(byte)1);if(Wire.available())Serial.println(Wire.read(),HEX);}delay(1000);}
```

**Output:** repeatable byte or `no ACK`. **Inference:** use the exact register map and initialization sequence from the part datasheet.

## SPI

```cpp
#include <SPI.h>
const byte CS=10;
void setup(){pinMode(CS,OUTPUT);digitalWrite(CS,HIGH);SPI.begin();Serial.begin(115200);}
byte readReg(byte r){digitalWrite(CS,LOW);SPI.transfer(r|0x80);byte v=SPI.transfer(0);digitalWrite(CS,HIGH);return v;}
void loop(){Serial.println(readReg(0x00),HEX);delay(500);}
```

**Output:** stable ID/status byte after correct mode/register/read bit are selected. **Inference:** verify SPI mode and protocol in the datasheet.

## Single-wire digital

For DS18B20, install `OneWire` and `DallasTemperature`; fit a 4.7 kΩ data pull-up. DHT needs its timing-specific library.

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire ow(2); DallasTemperature s(&ow);
void setup(){Serial.begin(115200);s.begin();}
void loop(){s.requestTemperatures();Serial.println(s.getTempCByIndex(0));delay(1000);}
```

**Output:** `24.50`-like °C (`-127.00` often means no probe). **Inference:** compare to an ice/ambient reference.

## 1-wire

Use [Single-wire digital](#single-wire-digital) for the DS18B20 library example.

## UART

For GPS and particulate sensors, cross TX/RX and use the documented baud rate.

```cpp
#include <SoftwareSerial.h>
SoftwareSerial sensor(2,3); // MCU RX, TX
void setup(){Serial.begin(115200);sensor.begin(9600);}
void loop(){while(sensor.available())Serial.write(sensor.read());}
```

**Output:** GPS emits `$G...` NMEA; PM sensors emit binary frames. **Inference:** bytes prove traffic, not a GPS fix or calibrated PM number—validate checksums/frames.

## Pulse timing

HC-SR04 ECHO is commonly 5 V: level-shift before a 3.3 V input.

```cpp
const byte TRIG=9,ECHO=8;
void setup(){pinMode(TRIG,OUTPUT);pinMode(ECHO,INPUT);Serial.begin(115200);}
void loop(){digitalWrite(TRIG,LOW);delayMicroseconds(2);digitalWrite(TRIG,HIGH);delayMicroseconds(10);digitalWrite(TRIG,LOW);unsigned long us=pulseIn(ECHO,HIGH,30000);Serial.println(us/58.0);delay(300);}
```

**Output:** `37.2`-like cm. **Inference:** target material, angle and air conditions affect returns.

## Digital threshold

```cpp
const byte IN=2;
void setup(){pinMode(IN,INPUT_PULLUP);Serial.begin(115200);}
void loop(){Serial.println(digitalRead(IN)?"OPEN/HIGH":"ACTIVE/LOW");delay(200);}
```

**Output:** state flips with motion/magnet/contact/threshold. **Inference:** confirm active polarity and allow PIR warm-up.

## Two-wire synchronous

For HX711 install an HX711 library and confirm load-cell wiring.

```cpp
#include "HX711.h"
HX711 scale;
void setup(){Serial.begin(115200);scale.begin(3,2);scale.tare();}
void loop(){Serial.println(scale.get_units(10));delay(500);}
```

**Output:** near zero after tare, repeatable change with load. **Inference:** calibrate using known mass and stable mechanics.

## I2S digital audio

I²S receive setup is board-specific. Start with the vendor’s 16 kHz mono RX example, then print a sample peak:

```cpp
// Configure I2S RX for your MCU first.
int32_t sample=readI2SSample();
Serial.println(abs(sample));
```

**Output:** peak rises with speech/clap. **Inference:** verify bit alignment, gain and sample rate before FFT/voice processing.

## Filtered telemetry and alarm

Replace `readSensor()` with a calibrated reading from a preceding recipe.

```cpp
float readSensor(){return analogRead(A0);} // replace
const float LIMIT=700; // establish from calibration
void setup(){Serial.begin(115200);}
void loop(){float sum=0;for(int i=0;i<5;i++){sum+=readSensor();delay(20);}float v=sum/5;Serial.print("value=");Serial.print(v,1);Serial.print(" state=");Serial.println(v>LIMIT?"CHECK":"NORMAL");delay(1000);}
```

**Output:** `value=486.2 state=NORMAL`. **Inference:** filtering reduces noise but delays response; thresholds need measured, calibrated data and a separately designed fail-safe.
