#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "pico/stdlib.h"
#include "hardware/gpio.h"

#define WIDTH 160 //240
#define HEIGHT 128 //320

#define LED_PIN 1

uint16_t framebuffer[WIDTH * HEIGHT];

static inline void put_pixel(int x, int y, uint8_t color) {
    framebuffer[y * WIDTH + x] = color;
}

void draw_line(int x0, int y0, int x1, int y1, uint8_t color) {
    int dx = abs(x1 - x0);
    int sx = x0 < x1 ? 1 : -1;

    int dy = -abs(y1 - y0);
    int sy = y0 < y1 ? 1 : -1;

    int err = dx + dy;

    while (1)
    {
        put_pixel(x0, y0, color);

        if (x0 == x1 && y0 == y1)
            break;

        int e2 = err * 2;

        if (e2 >= dy)
        {
            err += dy;
            x0 += sx;
        }

        if (e2 <= dx)
        {
            err += dx;
            y0 += sy;
        }
    }
}

int main()
{
    stdio_init_all();

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    gpio_put(LED_PIN, 0);
    
    sleep_ms(2000);

    while (true) {
        gpio_xor_mask(1u << LED_PIN);
        
        uint64_t start = time_us_64();

        memset(framebuffer, 0, sizeof(framebuffer));

        for (int i = 0; i < WIDTH; i++) {
            for (int ie = 0; ie < HEIGHT; ie++) {
                // draw_line(
                //     rand() % WIDTH,
                //     rand() % HEIGHT,
                //     rand() % WIDTH,
                //     rand() % HEIGHT,
                //     255
                // );
                put_pixel(i, ie, ((int) (i*ie+1155.0/2265)) % 65535);
            }
        }
    }
}