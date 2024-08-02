# Imports go at the top
from microbit import *
import random

ascore = 0
bscore = 0
starval = 0
# Code in a 'while True:' loop repeats forever
while True:
    winval = 0
    display.show(Image.DUCK)
    sleep(random.randint(1000, 4000))
    display.show(Image.HAPPY)
    winval = 1
    sleep(250)
    if button_a.is_pressed() and winval == 1:
        ascore = ascore + 1
    elif button_b.is_pressed() and winval == 1:
        bscore = bscore + 1
    elif bscore == 3:
        display.scroll('B wins!')
        sleep(5000)
        ascore = bscore = 0
    elif ascore == 3:
        display.scroll('A wins!')
        sleep(5000)
        ascore = bscore = 0
    