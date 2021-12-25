from abc import ABC
from itertools import chain

class LightProgram(ABC):
    def setup(self, *args, **kwargs):
        pass

    def loop(self):
        return None

    def flatten(self, nested_list):
        return list(
            chain(
                *[ele if isinstance(ele, list) else [ele] for ele in nested_list]
            )
        )

    def count(self):
        return self.strip.numPixels()


    def set_pixel(self, index, color):
        self.strip.setPixelColor(index, color)

    def show(self):
        self.strip.show()

    def pixel_range(self):
        return range(self.strip.numPixels())