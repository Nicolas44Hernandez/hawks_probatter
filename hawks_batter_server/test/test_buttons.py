from gpiozero import Button
from signal import pause
import time


def start_callback_function():
    time.sleep(0.2)
    print(f"Button start pressed")



button_start = Button(23, bounce_time=0.5) 
#button_start.when_pressed = start_callback_function

#pause()
while True: 
    print("Waitting...")
    button_start.wait_for_press()
    print("Button was pressed")

    button_start.wait_for_release(5)

    print("Button was released")