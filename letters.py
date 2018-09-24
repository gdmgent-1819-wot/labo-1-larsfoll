from sense_hat import SenseHat
from random import choice
from time import sleep
sense = SenseHat()

msg = input('Gimme some text: ')
speed = input('Gimme some speed: ')
speed = int(speed)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
colors = [red, blue, green]
index = len(msg)

def show_colored_letter(x):
    sense.show_letter(x, choice(colors))
    sleep(speed)

for letter in msg :
    show_colored_letter(letter)
    
