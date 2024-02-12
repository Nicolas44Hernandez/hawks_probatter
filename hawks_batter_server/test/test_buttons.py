from gpiozero import Button


def callback_function_start():
    print("Button start pressed")


def callback_function_end():
    print("Button end pressed")


button_start = Button(23)
button_end = Button(24)
button_start.when_pressed = callback_function_start
button_end.when_pressed = callback_function_end


while True: 
    a = 4