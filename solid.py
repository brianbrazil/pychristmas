import sys

from color import Color
from light_strip import LightStrip
from programs import Clear

if __name__ == '__main__':
    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])

    strip = LightStrip(200)
    strip.run(Clear(Color(red, green, blue)))
