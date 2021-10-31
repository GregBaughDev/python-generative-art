from PIL import Image
from noise import pnoise2
import random
import colorsys

class Artwork:
    def __init__(self, size=(500, 500), grain=0.5, noise_level=1.5, noise_shift=2.0):
        self.color = self.random_colour()
        self.palette = (
            self.random_colour(),
            self.random_colour(),
            self.random_colour(),
            self.random_colour(),
        )
        self.grain = grain
        self.noise_base = random.randint(0, 999)
        self.noise_level = noise_level
        self.noise_shift = noise_shift
        self.img = Image.new("RGBA", size)
        self.generate_art()

    def get_random_points(self):
        points = []
        for x in range(self.img.width):
            for y in range(self.img.height):
                points.append((x, y))

        random.shuffle(points)
        return points

    def generate_art(self):
        for (x, y) in self.get_random_points():
            color = self.get_colour_at_point(x, y)
            self.img.putpixel((x, y), color)

    def make_grain(self):
        if self.grain > 0:
            return random.uniform(-1 * self.grain, self.grain)
        else:
            return 0

    def make_noise(self, px, py):
        return self.noise_level * pnoise2(px * self.noise_shift, py * self.noise_shift, base=self.noise_base)

    def get_colour_at_point(self, x, y):
        (tl, tr, bl, br) = self.palette

        px = x / self.img.width
        py = y / self.img.height

        grain_x = self.make_grain()
        grain_y = self.make_grain()

        noise_x = self.make_noise(px, py)
        noise_y = self.make_noise(px, py)

        gradient1 = self.mix(tl, tr, px + grain_x + noise_x)
        gradient2 = self.mix(bl, br, px + grain_x + noise_x)
        rtn_gradient = self.mix(gradient1, gradient2, py + grain_y + noise_y)

        return rtn_gradient

    def mix(self, c1, c2, mix):
        (r1, g1, b1, a1) = c1
        (r2, g2, b2, a2) = c2

        mix = max(0, min(mix, 1))

        return (
            self.mix_channel(r1, r2, mix),
            self.mix_channel(g1, g2, mix),
            self.mix_channel(b1, b2, mix),
            self.mix_channel(a1, a2, mix)
        )

    def mix_channel(self, c1, c2, mix):
        return int(c1 + (c2 - c1) * mix)

    def random_colour(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 1)
        v = random.uniform(0.9, 1)

        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        return (r, g, b, 255)

    def generate(self, filepath):
        self.img.save(filepath)