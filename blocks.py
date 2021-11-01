from generate import Artwork
from PIL import ImageDraw
import os
import random

class Blocks(Artwork):
    def generate_art(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_points():
            color = self.get_colour_at_point(x, y)
            width = random.randint(2, 10)
            height = random.randint(2, 10)

            drawer.rectangle([
                (x - width, y - height), 
                (x + width, y + height)
            ], fill=color)

if __name__ == "__main__":
    os.makedirs("test", exist_ok=True)
    filepath = os.path.join("test", "art.png")
    art = Blocks()
    art.generate(filepath)
                