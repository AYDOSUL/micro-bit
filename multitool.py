from microbit import *
import music
import random
import time

compass.calibrate()
calibval = compass.get_field_strength()
while True:
    if pin_logo.is_touched():
        tuning = True
    else:
        tuning = False
    if accelerometer.was_gesture('shake') and tuning == True:
        speaker.on()
        music.pitch(440)
        display.show(Image.TRIANGLE)
        sleep(5000)
        speaker.off()
    elif button_b.is_pressed() and button_a.is_pressed() == False:
        degree = compass.heading()
        if degree < 45:
            display.show('N')
        elif degree < 135:
            display.show('E')
        elif degree < 225:
            display.show('S')
        elif degree < 315:
            display.show('W')
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(random.randint(1,6))
        sleep(1000)
        rand = random.randint(1,6)
        display.show(rand)
    elif button_a.is_pressed() and button_b.is_pressed() == False:
        if calibval < compass.get_field_strength():
            display.show(1)
        else:
            display.show(0)
    elif pin_logo.is_touched() and button_b.is_pressed():
        compass.calibrate()
    elif button_a.is_pressed() and pin_logo.is_touched():
        if button_a.is_pressed() and button_b.is_pressed and pin_logo.is_touched():
            display.show(round(time.ticks_ms()/1000))
    else:
        display.show(Image.HAPPY)
        speaker.off()