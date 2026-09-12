# MCU A

This RP2040 is responsible for managing user inputs, the smaller display, loading and playing music, as well as transmitting song information to `MCU B`!

Here's the pins:
- 0-3: SPI0 MCU
- 4-10: Buttons
- 11-14: Micro SD Card
- 16-17: UART0 MCU (backup)
- 18-19: OLED 128x32 Display
- 23-25: RGB, Board, Boot LEDS
- 20-22, 26-28: Audio