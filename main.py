from create import create
from lines import Lines
from blocks import Blocks
from circles import Circles

options = ["1. Create Pixel Art", "2. Create Square Art", "3. Create Circle Art", "4. Create Line Art"]

def user_options():
    qty = input("Please enter the number of images ")
    grain = input("Please enter a grain amount ")
    noise = input("Please enter a noise level ")
    return (int(qty), int(grain), int(noise))

print("-" * 100 + "\n" + "-" * 39 + "GENERATIVE ART CREATOR" + "-" * 39 + "\n" + "-" * 100)
print("Please choose from the following option:")

for option in options:
    print(option)

user_option = input("")
(qty, grain, noise) = user_options()

if int(user_option.strip()) == 1:
    create(image_count=qty + 1, grain=grain, noise_level=noise)
elif int(user_option.strip()) == 2:
    create(style=Blocks, image_count=qty + 1)
elif int(user_option.strip()) == 3:
    create(style=Circles, image_count=qty + 1)
elif int(user_option.strip()) == 4:
    create(style=Lines, image_count=qty + 1)
else:
    print("Input is not valid")