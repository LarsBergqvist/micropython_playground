# Alternating blinking of the two built-in LEDS
# on an Adafruit Huzzah board with MicroPython firmware

import machine, time

redled=machine.Pin(0,machine.Pin.OUT)
blueled=machine.Pin(2,machine.Pin.OUT)

while True:
    redled.high()
    blueled.low()
    time.sleep(1.0)
    redled.low()
    blueled.high()
    time.sleep(1.0)

