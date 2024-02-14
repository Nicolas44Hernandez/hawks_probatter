from gpiozero import Button
import time


def callback_function():
    print("Button pressed")
    time.sleep(2)



button = Button(23) 
button.when_pressed = callback_function


while True: 
    a = 4