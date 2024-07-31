from microbit import *
import music
import random
while True:
    if pin_logo.is_touched():
        tuning = True
    else:
        tuning = False
    if accelerometer.was_gesture('shake') and tuning == True:
        speaker.on()
        music.pitch(440)
        display.show(Image.TRIANGLE)
        sleep(2000)
        speaker.off()
    elif button_b.is_pressed():
        degree = compass.heading()
        if degree < 45:
            display.show('N')
        elif degree < 135:
            display.show('E')
        elif degree < 225:
            display.show('S')
        elif degree < 315:
            display.show('W')
    elif button_a.is_pressed():
        display.show(random.randint(1,6))
        sleep(1000)
        rand = random.randint(1,6)
        display.show(rand)
    else:
        display.show(Image.HAPPY)
        speaker.off()
