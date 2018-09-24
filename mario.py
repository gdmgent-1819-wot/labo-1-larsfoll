from sense_hat import SenseHat
from time import sleep
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


sense.set_pixels(mario)

mario_jump = [
    white, brown, brown, orange, orange, brown, orange, white,
    white, white, orange, orange, orange, orange, white, white,
    white, red, blue, red, red, blue, red, white,
    white, orange, blue, blue, blue, blue, orange, white,
    white, white, blue, blue, blue, blue, white, white,
    white, brown, brown, white, white, brown, brown, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white
]

def jump():
    sense.set_pixels(mario_jump)
    sleep(0.5)
    sense.set_pixels(mario)

sense.stick.direction_up = jump

while True:
    pass
