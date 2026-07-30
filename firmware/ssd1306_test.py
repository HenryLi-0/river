'''test to see best max frequency and refresh rate (i know, not exactly accurate)'''

import board
import busio
import displayio
import adafruit_displayio_ssd1306

displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000*1000)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=128,
    height=64,
)

import gc
import time

def showImage(filename):
    bitmap = displayio.OnDiskBitmap(filename)
    tilegrid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    group = displayio.Group()
    group.append(tilegrid)

    display.root_group = group
    gc.collect()

while True:
    showImage("z_processed2.bmp")
    time.sleep(0.03)
    showImage("z_processed3.bmp")
    time.sleep(0.03)
