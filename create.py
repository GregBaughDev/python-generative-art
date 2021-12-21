from generate import Artwork
from lines import Lines
from blocks import Blocks
from circles import Circles
import os

def create(grain, noise_level, image_count=11, style=Artwork):
    if style == Artwork:
        type = 'Pixels'
    elif style == Blocks:
        type = 'Squares'
    elif style == Circles:
        type = 'Circles'
    elif style == Lines:
        type = 'Lines'

    os.makedirs(str(type), exist_ok=True)

    print("Images generating")

    for i in range(1, image_count):
        print(f"Generating image {i}")
        filepath = os.path.join(str(type), f"{type}-{i}.png")

        art = style(noise_level, grain * 0.1)
        art.generate(filepath)

    print("Generating complete")

create(grain=0, noise_level=0.1, image_count=1, style=Lines)