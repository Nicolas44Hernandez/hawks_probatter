from gpiozero import Button
import time


def callback_function(button_number):
    print(f"Button pressed: {button_number}")
    if button_number.pin == 23:
        print("button_number == 23")
    time.sleep(1)



button = Button(23) 
button.when_pressed = callback_function


while True: 
    a = 4