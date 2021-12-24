import random
import time
from color import Color
from light_program import LightProgram

class RainbowTwinkle(LightProgram):
    def setup(self):
        self.colors = Color.RAINBOW + [Color.BLACK]
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, random.choice(self.colors))
            self.strip.show()

    def loop(self):
        for i in random.choices(range(self.strip.numPixels()), k=random.randrange(8)):
            self.strip.setPixelColor(i, random.choice(self.colors))
        time.sleep(random.randrange(1, 5) / 10000)
        self.strip.show()

class Chase(LightProgram):
    def __init__(self, colors, sleep=0.5):
        colors = self.flatten(colors)
        colors.reverse()
        self.colors = colors
        self.sleep = sleep
        self.switch = 0

    def loop(self):
        self.switch = (self.switch + 1) % len(self.colors)
        for i in range(self.strip.numPixels()):
            color = self.colors[(i - self.switch) % len(self.colors)]
            self.strip.setPixelColor(i, color)
        self.strip.show()
        time.sleep(self.sleep)