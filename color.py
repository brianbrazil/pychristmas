# from rpi_ws281x import Color as OrigColor
from random import randrange
import pdb

class Color(int):
    def __new__(cls, value, *args, **kwargs):
        red = value
        green = args[0]
        blue = args[1]
        code = (green << 16) | (red << 8) | blue
        return super().__new__(cls, code)

Color.RED = Color(255, 0, 0)
Color.ORANGE = Color(255, 163, 0)
Color.YELLOW = Color(255, 255, 0)
Color.GREEN = Color(0, 255, 0)
Color.BLUE = Color(0, 0, 255)
Color.PURPLE = Color(83, 0, 83)

Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(255, 245, 245)
Color.WARM_WHITE = Color(255, 147, 44)
Color.PINK = Color(255, 25, 25)
Color.LIGHT_PINK = Color(255, 50, 50)

Color.RAINBOW = [
    Color.RED,
    Color.ORANGE,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.PURPLE
]