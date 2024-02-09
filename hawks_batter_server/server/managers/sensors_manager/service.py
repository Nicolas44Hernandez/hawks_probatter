import logging
import time
from flask import Flask
from server.interfaces.gpio_interface.service import GpioButtonInterface
from server.managers.video_manager import video_manager_service

logger = logging.getLogger(__name__)


class SensorsManager:
    """Manager for Sensors detection peripheral"""

    button_1_interface: GpioButtonInterface
    button_2_interface: GpioButtonInterface

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize SensorsManager"""
        if app is not None:
            logger.info("initializing the SensorsManager")

            self.button_1_interface = GpioButtonInterface(
                button_pin=app.config["SENSOR_START_PIN"],
                callback_function=self.start_callback,
            )

            self.button_2_interface = GpioButtonInterface(
                button_pin=app.config["SENSOR_STOP_PIN"],
                callback_function=self.end_callback,
            )

    def start_callback(self, channel):
        """Callback function for button 1 detection"""
        logger.info(f"Button start pressed")
        # Sensor debounce
        time.sleep(0.2)
        video_manager_service.run_video()
    
    def end_callback(self, channel):
        """Callback function for button 2 detection"""
        logger.info(f"Button stop pressed")
        # Sensor debounce
        time.sleep(0.2)
        video_manager_service.stop_video()        


sensors_manager_service: SensorsManager = SensorsManager()
""" Sensors manager service singleton"""
