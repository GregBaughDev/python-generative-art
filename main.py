from create import create
from lines import Lines
from blocks import Blocks
from circles import Circles

options = ["1. Create Pixel Art", "2. Create Square Art", "3. Create Circle Art", "4. Create Line Art"]

print("-" * 100 + "\n" + "-" * 39 + "GENERATIVE ART CREATOR" + "-" * 39 + "\n" + "-" * 100)
print("Please choose from the following option:")

for option in options:
    print(option)

user_option = input("")

if int(user_option.strip()) == 1:
    create()
elif int(user_option.strip()) == 2:
    create(style=Blocks)
elif int(user_option.strip()) == 3:
    create(style=Circles)
elif int(user_option.strip()) == 4:
    create(style=Lines)