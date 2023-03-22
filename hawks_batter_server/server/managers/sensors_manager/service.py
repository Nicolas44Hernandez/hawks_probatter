import logging
import time
from flask import Flask
from server.interfaces.gpio_interface.service import GpioMotionSensorInterface
from server.managers.video_manager import video_manager_service

logger = logging.getLogger(__name__)


class SensorsManager:
    """Manager for Sensors detection peripheral"""

    sensor_1_interface: GpioMotionSensorInterface
    sensor_1_interface: GpioMotionSensorInterface

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize SensorsManager"""
        if app is not None:
            logger.info("initializing the SensorsManager")

            self.sensor_1_interface = GpioMotionSensorInterface(
                sensor_pin=app.config["SENSOR_START_PIN"],
                callback_function=self.sensor_start_callback,
            )

            self.sensor_2_interface = GpioMotionSensorInterface(
                sensor_pin=app.config["SENSOR_START_PIN"],
                callback_function=self.sensor_end_callback,
            )

    def sensor_start_callback(self, channel):
        """Callback function for sensor 1 detection"""
        # Sensor debounce
        time.sleep(0.2)
        video_manager_service.run_video()
    
    def sensor_end_callback(self, channel):
        """Callback function for sensor 2 detection"""
        # Sensor debounce
        time.sleep(0.2)
        video_manager_service.stop_video()


        


sensors_manager_service: SensorsManager = SensorsManager()
""" Sensors manager service singleton"""
