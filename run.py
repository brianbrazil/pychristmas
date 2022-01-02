from light_strip import LightStrip
from color import Color
from programs import Chase, Twinkle, CrossFade

COLORS = [
    [Color.BLACK] * 3,
    Color.CLASSIC
]

if __name__ == '__main__':
    strip = LightStrip(200)
    strip.run(Chase(COLORS, sleep=0.3))
    # strip.run(Twinkle(COLORS))
    # strip.run(CrossFade(COLORS))