import logging
import time
from flask import Flask
from server.interfaces.gpio_interface.service import GpioButtonInterface
from server.managers.video_manager import video_manager_service

logger = logging.getLogger(__name__)


class SensorsManager:
    """Manager for Sensors detection peripheral"""

    button_1_interface: GpioButtonInterface
    start_button_pin: int

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize SensorsManager"""
        if app is not None:
            logger.info("initializing the SensorsManager")
            
            self.start_button_pin = app.config["SENSOR_START_PIN"]

            self.enable_button()
            

    def start_callback(self):
        """Callback function for button 1 detection"""
        # Sensor debounce
        logger.info("start button callback")
        self.disable_button()
        time.sleep(0.2)
        if video_manager_service.video_capture_interface.waiting_for_start:
            video_manager_service.start_pitch()      
            time.sleep(3)
            self.enable_button()


    def disable_button(self):
        """Disable button"""
        self.button_1_interface = None


    def enable_button(self):
        """Enable button"""
        self.button_1_interface = GpioButtonInterface(
            button_pin=self.start_button_pin,
            callback_function=self.start_callback,
        )

sensors_manager_service: SensorsManager = SensorsManager()
""" Sensors manager service singleton"""
