from gpiozero import Button
import time

global b_active

def callback_function():
    global b_active
    if b_active:
        b_active=False
        print("Button pressed")
        time.sleep(1)
        b_active=True



b_active=True
button = Button(23, pull_up=True, bounce_time=1) 
button.when_pressed = callback_function


while True: 
    a = 4