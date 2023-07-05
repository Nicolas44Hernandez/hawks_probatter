"""
GPIO interface service
"""
import logging
import time
from gpiozero import Button, LED

logger = logging.getLogger(__name__)


class GpioButtonInterface:
    """Service class for RPI Button GPIO"""

    button_pin: int
    button: Button
    callback_function: callable

    def __init__(self, button_pin: int, callback_function: callable):

        logger.info(f"Creating RPI GpioButtonInterface interface:")
        logger.info(f"button_pin: {button_pin}")
        logger.info(f"callback_function: {callback_function}")

        self.button_pin = button_pin

        # setup
        self.button = Button(self.button_pin)
        self.button.when_pressed = callback_function
        
class GpioMachineOutputInterface:
    """Service class for RPI Output GPIO"""

    start_pin: int
    stop_pin: int
    start_output: LED
    stop_output: LED

    def __init__(self, start_pin: int, stop_pin: int):

        logger.info(f"Creating RPI GPIO Output interface:")
        logger.info(f"start_pin: {start_pin}")
        logger.info(f"stop_pin: {stop_pin}")

        self.start_pin = start_pin
        self.stop_pin = stop_pin

        # setup
        self.start_output = LED(self.start_pin)
        self.stop_output = LED(self.stop_pin)
        self.start_output.on()
        self.stop_output.on()

    def start_machine(self):
        """Start ptching machine"""
        self.start_output.off()
        time.sleep(0.5)
        self.start_output.on()
    
    def stop_machine(self):
        """Start ptching machine"""
        self.stop_output.off()
        time.sleep(0.5)
        self.stop_output.on()

