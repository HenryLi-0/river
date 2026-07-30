'''test to see a reasonable size and the impact on performance for various bitmap settings'''

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_character_lcd.character_lcd import Character_LCD
import displayio
import bitmaptools

boardLED = DigitalInOut(board.LED)
boardLED.direction = Direction.OUTPUT
boardLED.value = True

redLED = DigitalInOut(board.GP1)
redLED.direction = Direction.OUTPUT
redLED.value = True

size = 128
colors = 256
bitmap = displayio.Bitmap(size, size, colors)

while True:
    redLED.value = not(redLED.value)
    bitmap.fill(0)
    for i in range(100):
        bitmaptools.draw_line(bitmap, 0, 0, size - 1, size - 1, i)