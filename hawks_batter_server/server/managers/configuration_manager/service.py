"""
Configuration service
"""
import logging
from server.managers.video_manager import video_manager_service

logger = logging.getLogger(__name__)


class ConfigurationService:
    """Service class for video manager"""

    def get_current_configuration(self):
        """Get current video manager configuration"""
        return video_manager_service.get_current_configuration()
    
    def set_configuration(self, pitches: int, video: str):
        """Set configuration"""
        return video_manager_service.set_configuration(video=video, pitches=pitches)


configuration_service: ConfigurationService = ConfigurationService()
""" ConfigurationService service singleton"""
