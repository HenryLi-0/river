'''this should be rewritten in c for better performance!'''

import board
import digitalio
import busio
import time

import displayio

'''DOUBLE CHECK THESE PINS'''
class Constants:
    class CPU_SPI:
        SCK = board.GP0
        MOSI = board.GP2
        MISO = board.GP1
        CS = board.GP3

    class CPU_UART:
        TX = board.GP17
        RX = board.GP16

    class TFT:
        DC = board.GP8
        CS = board.GP9
        SCK = board.GP10
        MOSI = board.GP11
        RST = board.GP12
        BL = board.GP13

    class LEDS:
        RGB = board.GP23
        BOARD = board.GP24
        BOOT = board.GP25

led = digitalio.DigitalInOut(Constants.LEDS.BOOT)
led.direction = digitalio.Direction.OUTPUT
led.value = True

class MCU_B:
    def __init__(self):
        # self.setupSPI()
        self.setupUART()

        self.setupDisplay()

    # setup comms (in theory)
    def setupUART(self):
        self.uart = busio.UART(
            Constants.CPU_UART.TX,
            Constants.CPU_UART.RX # where does baudrate come in
        )
    def setupSPI(self):
        self.spi = busio.SPI(
            Constants.CPU_SPI.SCK,
            Constants.CPU_SPI.MOSI,
            Constants.CPU_SPI.MISO
        )
    def send(self):
        if self.uart is None:
            self.setupUART()
        # ???

    def setupDisplay(self):
        self.displaySPI = busio.SPI(
            Constants.TFT.SCK,
            MOSI = Constants.TFT.MOSI
        )
        self.display = displayio.FourWire( #??? idk if this is correct
            self.displaySPI,
            command = Constants.TFT.DC,
            chip_select = Constants.TFT.CS,
            reset = Constants.TFT.RST,
        )

mcu = MCU_B()
