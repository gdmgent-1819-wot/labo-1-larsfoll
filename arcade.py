from random import choice
import threading
from sense_hat import SenseHat
sense = SenseHat()

red = (233, 63, 51)
brown = (71, 35, 8)
orange = (248, 194, 51)
yellow = (255, 244, 50)
blue = (36, 74, 251)
white = (255, 255, 255)
black = (0, 0, 0)

mario = [
    white, white, red, red, red, red, white, white,
    white, white, brown, orange, black, orange, white, white,
    white, brown, brown, orange, orange, brown, orange, white,
    white, white, orange, orange, orange, orange, white, white,
    white, red, blue, red, red, blue, red, white,
    white, orange, blue, blue, blue, blue, orange, white,
    white, white, blue, blue, blue, blue, white, white,
    white, brown, brown, white, white, brown, brown, white,
]

pacman = [
    black, black, black, black, black, black, black, black,
    black, black, yellow, yellow, yellow, yellow, black, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, yellow, black, black, black, black, black, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, black, yellow, yellow, yellow, yellow, black, black,
    black, black, black, black, black, black, black, black
]

ghost = [
    black, black, black, black, black, black, black, black,
    black, black, yellow, yellow, yellow, yellow, black, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, yellow, white, yellow, yellow, white, yellow, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, yellow, yellow, yellow, yellow, yellow, yellow, black,
    black, yellow, black, yellow, yellow, black, yellow, black,
    black, black, black, black, black, black, black, black
]

characters = [mario, pacman, ghost]

def random_character():
    threading.Timer(3.0, random_character).start()
    sense.set_pixels(choice(characters))

random_character()