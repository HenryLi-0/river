import board
import digitalio
import time

import storage
import adafruit_sdcard

# ??? still need to understand these docs

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

# so uh, i cant actually write any of this without the actual thing