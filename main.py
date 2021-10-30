from generate import Artwork
import os

os.makedirs('test', exist_ok=True)

print("Images generating")

for i in range(1, 11):
    print(f"Generating image {i}")
    filepath = os.path.join("test", f"test-{i}.png")

    art = Artwork(grain=i * 0.1)
    art.generate(filepath)

print("Generating complete")