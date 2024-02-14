from gpiozero import Button
import time


def start_callback_function(button_number):
    print(f"Button pressed: {button_number}")
    print(f"pin: {button_number.pin}")
    print(f"type(pin): {type(button_number.pin)}")
    if button_number.pin == 23:
        print("button_number == 23")
    time.sleep(1)



button_start = Button(23) 
button_end = Button(24) 
button_start.when_pressed = start_callback_function
button_end.when_pressed = start_callback_function


while True: 
    a = 4