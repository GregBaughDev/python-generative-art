import os
from generate import Artwork

os.makedirs('exports', exist_ok=True)

filepath = os.path.join("exports", f"export.png")

art = Artwork(size=(2000, 2000))
art.generate(filepath)