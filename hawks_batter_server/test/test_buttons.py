from gpiozero import Button
from signal import pause
import time


def start_callback_function():
    time.sleep(0.2)
    print(f"Button start pressed")



button_start = Button(23) 
button_start.when_pressed = start_callback_function

pause()
# while True: 
#     if button_start.is_pressed:
#         print("Button start is pressed")
    # if button_end.is_pressed:
    #     print("Button end is pressed")
    #time.sleep(1)
    #print("Waitting...")
    #a =2