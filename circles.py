from generate import Artwork
from PIL import ImageDraw
import os
import random

class Circles(Artwork):
    def generate_art(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_points():
            color = self.get_colour_at_point(x, y)
            radius = random.randint(2, 10)

            drawer.ellipse([
                (x - radius, y - radius), 
                (x + radius, y + radius)
            ], fill=color)

if __name__ == "__main__":
    os.makedirs("circles", exist_ok=True)
    filepath = os.path.join("circles", "1.png")
    art = Circles()
    art.generate(filepath)
                