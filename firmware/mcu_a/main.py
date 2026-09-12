import board
import digitalio
import busio
import time
import os

import storage
import sdcardio

import displayio
import terminalio
import adafruit_displayio_ssd1306 #??? idk maybe

import audiomp3
import audiopwmio

# ??? still need to understand these docs

'''DOUBLE CHECK THESE PINS'''
class Constants:
    BUTTONS = [board.GP4, board.GP5, board.GP6]

    class GPU_SPI:
        SCK = board.GP0
        MOSI = board.GP1
        MISO = board.GP2
        CS = board.GP3

    class GPU_UART:
        TX = board.GP16
        RX = board.GP17

    class SD:
        SCK = board.GP11
        MOSI = board.GP12
        MISO = board.GP13
        CS = board.GP14

        DIR = "/sd" # ???
        EXTENSIONS = [".mp3", ".wav"]

    class OLED:
        SCL = board.GP18
        SDA = board.GP19

    class LEDS:
        RGB = board.GP23
        BOARD = board.GP24
        BOOT = board.GP25

    class AUDIO:
        pass

led = digitalio.DigitalInOut(Constants.LEDS.BOOT)
led.direction = digitalio.Direction.OUTPUT
led.value = True

class MCU_A:
    def __init__(self):
        # self.setupSPI()
        self.setupUART()

    # setup comms (in theory)
    def setupUART(self):
        self.uart = busio.UART(
            Constants.GPU_UART.TX,
            Constants.GPU_UART.RX # where does baudrate come in
        )
    def setupSPI(self):
        self.spi = busio.SPI(
            Constants.GPU_SPI.SCK,
            Constants.GPU_SPI.MOSI,
            Constants.GPU_SPI.MISO
        )
    def send(self):
        if self.uart is None:
            self.setupUART()
        # ???

    def setupSD(self):
        self.sdSPI = busio.SPI(
            Constants.SD.SCK,
            Constants.SD.MOSI,
            Constants.SD.MISO
        )
        self.sd = sdcardio.SDCard(
            self.sdSPI,
            Constants.SD.CS # where does baudrate come in
        )

        '''TODO mount and read the sd card???'''


    def setupPlay(self):
        self.pause = False
        self.songID = 0
        # pick first song idk

    def play(self):
        self.pause = False

    def stop(self):
        self.pause = False
        # ???
    

mcu = MCU_A()

# some update loop for the user stuff