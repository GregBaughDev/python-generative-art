from generate import Artwork
import os

os.makedirs('test', exist_ok=True)

for i in range(1, 11):
    filepath = os.path.join("test", f"test-{i}.png")

    art = Artwork()
    art.generate(filepath)