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

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize VideoManager"""
        if app is not None:
            logger.info("initializing the VideoManager")
            self.video_capture_interface = VideoCaptureInterface(
                video=app.config["DEFAULT_VIDEO"], 
                setup_frame=app.config["SETUP_FRAME"]
            )

            self.video_capture_interface.start()
    
    def run_video(self):
        """Launch video"""
        self.video_capture_interface.run_video()

    def stop_video(self):
        """Stop video"""
        self.video_capture_interface.stop_video()


video_manager_service: VideoManager = VideoManager()
""" VideoManager  service singleton"""
