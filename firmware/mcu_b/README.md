# MCU B

This RP2040 is responsible for displaying the graphics on the central display, after receiving song information to `MCU A`!

Here's the pins:
- 0-3: SPI0 MCU
- 8-13: LCD 128x160 Display
- 16-17: UART0 MCU (backup)
- 23-25: RGB, Board, Boot LEDS