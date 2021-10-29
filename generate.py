import random
from PIL import Image

class Artwork:
    def __init__(self, size=(500, 500)):
        self.r = self.random_colour()
        self.g = self.random_colour()
        self.b = self.random_colour()
        self.a = 255
        self.img = Image.new("RGBA", size, color=(self.r, self.g, self.b, self.a))

    def random_colour(self):
        return random.randint(100, 255)

    def generate(self, filepath):
        self.img.save(filepath)