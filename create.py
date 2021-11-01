from generate import Artwork
from lines import Lines
from blocks import Blocks
from circles import Circles
import os

# TO DO: Create CLI program for user input

def create(image_count=11, style=Artwork):
    os.makedirs('test', exist_ok=True)

    print("Images generating")

    for i in range(1, image_count):
        print(f"Generating image {i}")
        filepath = os.path.join("test", f"test-{i}.png")

        art = style(grain=i * 0.1)
        art.generate(filepath)

    print("Generating complete")