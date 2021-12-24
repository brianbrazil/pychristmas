from light_strip import LightStrip
from color import Color
from my_programs import Chase, RainbowTwinkle

COLORS = [
    [Color.BLACK] * 2,
    Color.RAINBOW
]

if __name__ == '__main__':
    strip = LightStrip(200)
    # strip.run_program(Chase(COLORS, sleep=0.1))
    strip.run(RainbowTwinkle())
