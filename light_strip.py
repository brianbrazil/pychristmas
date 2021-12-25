from rpi_ws281x import PixelStrip
from color import Color

class LightStrip:
    def __init__(self, count, pin=18, freq_hz=800000, dma=10, brightness=255, invert=False, channel=0):
        self.count = count
        self.strip = PixelStrip(count, pin, freq_hz, dma, invert, brightness, channel)
        self.strip.begin()

    def run(self, light_program):
        light_program.strip = self
        light_program.setup()
        try:
            while True:
                light_program.loop()
        except:
            self.blackout()

    def numPixels(self):
        return self.count

    def setPixelColor(self, i, color):
        self.strip.setPixelColor(i, color)

    def show(self):
        self.strip.show()

    def blackout(self):
        for i in range(self.numPixels()):
            self.strip.setPixelColor(i, Color.BLACK)
        self.strip.show()