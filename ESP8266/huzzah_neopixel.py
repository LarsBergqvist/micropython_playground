#
# A script for an Adafruit Huzzah (ESP8266) with a NeoPixel ring attached
#
from machine import Pin
from neopixel import NeoPixel
import time

OUTPUTPIN = 14          # use GPIO14 as output to NeoPixel ring
NUMPIXELS = 12          # number of pixels in NeoPixel ring
pin = Pin(OUTPUTPIN, Pin.OUT)   
np = NeoPixel(pin, NUMPIXELS)

def from_dark_to_light(pixel):
        for light in range(0,200,100):
            np[pixel] = (light,int(light/4),int(light/3))
            time.sleep(0.01)
            np.write()

previousPixel = 0
while True:
    for pixel in range(0,NUMPIXELS):
        np[previousPixel] = (0,0,0)
        from_dark_to_light(pixel)
        previousPixel=pixel
    for pixel in range(NUMPIXELS-2,0,-1):
        np[previousPixel] = (0,0,0)
        from_dark_to_light(pixel)
        previousPixel=pixel
