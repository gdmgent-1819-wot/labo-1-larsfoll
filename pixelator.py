from random import choice, randint
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

sense.clear()

def light_up(x, y):
    color = (randint(0, 255), randint(0, 255),randint(0, 255))
    sense.set_pixel(x, y, color)
    sleep(0.01)  
    
def loop_matrix():
    for y in range (0, 8):
        for x in range(0, 8):
            light_up(x,y)
            sense.clear()
            current = x * y
            if current == 49:
                loop_matrix()

loop_matrix()