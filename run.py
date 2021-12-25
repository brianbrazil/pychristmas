from light_strip import LightStrip
from color import Color
from programs import Chase, Twinkle

COLORS = [
    [Color.BLACK] * 5,
    Color.RAINBOW
]

if __name__ == '__main__':
    strip = LightStrip(200)
    # strip.run(Chase(COLORS, sleep=0.1))
    strip.run(Twinkle(COLORS))