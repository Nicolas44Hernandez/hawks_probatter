"""
GPIO interface service
"""
import logging
import time
from gpiozero import MotionSensor, LED

logger = logging.getLogger(__name__)


class GpioMotionSensorInterface:
    """Service class for RPI Button GPIO"""

    sensor_pin: int
    motion_sensor: MotionSensor
    callback_function: callable

    def __init__(self, sensor_pin: int, callback_function: callable):

        logger.info(f"Creating RPI GPIO MotionSensor interface:")
        logger.info(f"button_pin: {sensor_pin}")
        logger.info(f"callback_function: {callback_function}")

        self.sensor_pin = sensor_pin

        # setup
        self.motion_sensor = MotionSensor(self.sensor_pin)
        # sensor output  is inverted
        self.motion_sensor.when_no_motion = callback_function

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
        time.sleep(1)
        self.start_output.on()
    
    def stop_machine(self):
        """Start ptching machine"""
        self.stop_output.off()
        time.sleep(1)
        self.stop_output.on()

