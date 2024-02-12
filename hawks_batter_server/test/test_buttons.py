from gpiozero import Button
import time


def callback_function_start():
    print("Button start pressed")
    time.sleep(0.5)


def callback_function_end():
    print("Button end pressed")
    time.sleep(0.5)


#button_start = Button(23)
button_end = Button(24, bounce_time = 1)
#button_start.when_pressed = callback_function_start
button_end.when_pressed = callback_function_end


while True: 
    a = 4