"""
Video manager service
"""
import logging
from flask import Flask
from server.interfaces.video_capture_interface import VideoCaptureInterface

logger = logging.getLogger(__name__)


class VideoManager:
    """Service class for video manager"""

    video_capture_interface: VideoCaptureInterface
    reimaning_pitches: int
    total_pitches: int

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize VideoManager"""
        if app is not None:
            logger.info("initializing the VideoManager")

            self.total_pitches=app.config["DEFAULT_NUMBER_OF_PITCHES"]
            self.reimaning_pitches = self.total_pitches

            logger.info(f"Default number of pitches: {self.total_pitches}")

            self.video_capture_interface = VideoCaptureInterface(
                video=app.config["DEFAULT_VIDEO"], 
                setup_frame=app.config["SETUP_FRAME"],
                startup_frame=app.config["STARTUP_FRAME"],
            )

            self.video_capture_interface.start()
    
    def run_video(self):
        """Launch video"""
        if self.reimaning_pitches > 0:
            self.video_capture_interface.run_video(self.reimaning_pitches)
            self.reimaning_pitches = self.reimaning_pitches - 1
        else: 
            logger.info("Game is over. Restar from website or manually")
            self.video_capture_interface.end_game()
            self.reimaning_pitches = self.total_pitches
        
    def stop_video(self):
        """Stop video"""
        self.video_capture_interface.stop_video()

    
    # def set_number_of_pitches(self, number_of_pitches: int):
    #     """Set machine number of pitches"""
    #     if self.video_capture_interface.:
    #         self.total_pitches = number_of_pitches


video_manager_service: VideoManager = VideoManager()
""" VideoManager  service singleton"""
