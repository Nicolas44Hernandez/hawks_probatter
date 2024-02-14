from gpiozero import Button
import time


def callback_function(button_number):
    print(f"Button pressed: {button_number}")
    time.sleep(1)



button = Button(23) 
button.when_pressed = callback_function


while True: 
    a = 4