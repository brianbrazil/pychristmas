import sys

from rpi_ws281x import PixelStrip
from color import Color

LED_COUNT = 200        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

if __name__ == '__main__':
    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        clear(strip, Color(red, green, blue))
        # twinkle(strip)
        # while True:
        #     rainbowCycle(strip, 5)
    except KeyboardInterrupt:
        clear(strip, Color(0, 0, 0))