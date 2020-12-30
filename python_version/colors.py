import random

# Some useful colors
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

def get_random_color():
    first = random.randrange(256)
    second = random.randrange(256)
    third = random.randrange(256)
    return first, second, third
