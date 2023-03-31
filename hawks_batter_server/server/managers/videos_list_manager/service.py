import logging
from typing import Iterable
import yaml
from flask import Flask

logger = logging.getLogger(__name__)

class Video:
    name: str
    path: str
    
    def __init__(self,name: str, path: str):
        self.name = name
        self.path = path

class VideosListManager:
    """Manager for videos list"""

    configuration_file: str
    videos_list: Iterable[Video]

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize VideosListManager"""
        if app is not None:
            logger.info("initializing the VideosListManager")
            self.configuration_file = app.config["VIDEOS_CONFIGURATION_FILE"]

            # Load Videos configuration
            with open(self.configuration_file) as stream:
                try:
                    configuration = yaml.safe_load(stream)                    
                    self.videos_list = [
                        Video(
                            name=video["name"],
                            path=video["path"],
                        )
                        for video in configuration["VIDEOS"]
                    ]
                except (yaml.YAMLError, KeyError):
                    logger.error("Error in videos list configuration load, check file")
                            

    def get_video_path(self, video_name:str):
        """get path for a video"""
        logger.info(f"Searching path for video: {video_name}")
        for video in self.videos_list:
            if video.name == video_name:
                return video.path
            
        logger.error("video not found")
        return False  

    def get_videos_list(self):
        """Returns the list of videos available"""   
        logger.info("Retrieve videos list")
        return self.videos_list

videos_list_manager_service: VideosListManager = VideosListManager()
""" Videos list manager service singleton"""
