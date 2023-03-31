import logging
from flask import Flask
from server.interfaces.gpio_interface.service import GpioMachineOutputInterface

logger = logging.getLogger(__name__)


class MachineManager:
    """Manager for Machine start and stop"""

    machine_manager: GpioMachineOutputInterface

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize MachineManager"""
        if app is not None:
            logger.info("initializing the MachineManager")

            self.machine_manager = GpioMachineOutputInterface(
                start_pin=app.config["MACHINE_START_PIN"],
                stop_pin=app.config["MACHINE_STOP_PIN"],
            )

    def start_machine(self):
        """Start machine"""
        self.machine_manager.start_machine()

    def stop_machine(self):
        """Stop machine"""
        self.machine_manager.stop_machine()        


machine_manager_service: MachineManager = MachineManager()
""" Machine manager service singleton"""
