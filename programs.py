import random
import time
from color import Color
from light_program import LightProgram

class Chase(LightProgram):
    def __init__(self, colors, sleep=0.5):
        colors = self.flatten(colors)
        colors.reverse()
        self.colors = colors
        self.sleep = sleep
        self.switch = 0

    def loop(self):
        self.switch = (self.switch + 1) % len(self.colors)
        for i in self.pixel_range():
            color = self.colors[(i - self.switch) % len(self.colors)]
            self.set_pixel(i, color)
        self.show()
        time.sleep(self.sleep)

class Clear(LightProgram):
    def __init__(self, color):
        self.color = color

    def setup(self):
        for i in self.pixel_range():
            self.set_pixel(i, self.color)
        self.show()

class Flood(LightProgram):
    def __init__(self, color):
        self.color = color

    def setup(self):
        for i in self.pixel_range():
            self.set_pixel(i, self.color)
            self.show()

class Twinkle(LightProgram):
    def __init__(self, colors):
        self.colors = self.flatten(colors)

    def setup(self):
        for i in range(self.count()):
            self.set_pixel(i, random.choice(self.colors))
        self.show()

    def loop(self):
        for i in random.choices(range(self.count()), k=random.randrange(int(self.count()/15))):
            self.set_pixel(i, random.choice(self.colors))
        time.sleep(random.randrange(8, 15) / 10000)
        self.show()
