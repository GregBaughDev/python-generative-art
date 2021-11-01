from generate import Artwork
from PIL import ImageDraw
import os
import random
import math

class Lines(Artwork):
    def generate_art(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_points():
            color = self.get_colour_at_point(x, y)
            length = random.randint(2, 10)
            angle = random.uniform(0, 3.141)

            sx = length * math.sin(angle)
            sy = length * math.cos(angle)

            drawer.line([
                (x - sx, y - sy), 
                (x + sx, y + sy)
            ], fill=color)

if __name__ == "__main__":
    os.makedirs("test", exist_ok=True)
    filepath = os.path.join("test", "art.png")
    art = Lines()
    art.generate(filepath)
                