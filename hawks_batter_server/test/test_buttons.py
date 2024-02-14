from gpiozero import Button, pins
import time
global running

def start_callback_function():
    global running
    if not running:
        print(f"Button start pressed")
        print(f"Waitting for end button press")
        running = True

def end_callback_function():
    global running
    if running:
        print(f"Button end pressed")
        print(f"Waitting for start button press")
        running = False



button_start = Button(23) 
button_end = Button(24) 
button_start.when_pressed = start_callback_function
button_end.when_pressed = end_callback_function
running = False

while True: 
    a = 4