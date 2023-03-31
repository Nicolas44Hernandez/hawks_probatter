"""
Video manager service
"""
import logging
from flask import Flask
from server.interfaces.video_capture_interface import VideoCaptureInterface
from server.interfaces.keyboard_input_interface import KeyboardInputInterface
from server.managers.machine_manager import machine_manager_service
from server.managers.videos_list_manager import videos_list_manager_service


logger = logging.getLogger(__name__)


class VideoManager:
    """Service class for video manager"""

    video_capture_interface: VideoCaptureInterface
    keboard_input_interface: KeyboardInputInterface
    reimaning_pitches: int
    total_pitches: int
    video: str

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize VideoManager"""
        if app is not None:
            logger.info("initializing the VideoManager")

            self.total_pitches=app.config["DEFAULT_NUMBER_OF_PITCHES"]
            self.reimaning_pitches = self.total_pitches
            self.video = app.config["DEFAULT_VIDEO"]

            logger.info(f"Default number of pitches: {self.total_pitches}")            

            self.keboard_input_interface = KeyboardInputInterface(
                setup_callback=self.setup_image, 
                run_callback=self.new_game, 
                exit_callback=self.exit_game, 
                new_video_callback=self.set_new_video
            )

            self.video_capture_interface = VideoCaptureInterface(
                video=videos_list_manager_service.get_video_path(self.video), 
                setup_frame=app.config["SETUP_FRAME"],
                startup_frame=app.config["STARTUP_FRAME"],
            )

            self.video_capture_interface.start()
        

    def run_video(self):
        """Launch video"""
        if self.reimaning_pitches == self.total_pitches:
            self.video_capture_interface.start_game()
        self.video_capture_interface.run_video(self.reimaning_pitches)        
        
    def stop_video(self):
        """Stop video"""
        # Stop video
        self.video_capture_interface.stop_video()
        self.reimaning_pitches = self.reimaning_pitches - 1
        
        # Evaluate if game is over
        if self.reimaning_pitches <= 0:
            logger.info("Game is over. Restar from website or manually")
            self.video_capture_interface.end_game()
            self.reimaning_pitches = self.total_pitches
                    
    def setup_image(self):
        """Setup image"""
        if not self.video_capture_interface.setting_up:
            logger.info("Setting up image")
            self.video_capture_interface.set_up_image(True)
        else:
            logger.info("Setting up image done")
            self.video_capture_interface.set_up_image(False)
            self.reimaning_pitches = self.total_pitches

    def new_game(self):
        """New game"""
        self.reimaning_pitches = self.total_pitches
        if not self.video_capture_interface.running:
            logger.info("New game")
            machine_manager_service.start_machine()
            self.video_capture_interface.start_game()

    def exit_game(self):
        """Exit game """         
        if self.video_capture_interface.running:
            logger.info("Game over")
            self.video_capture_interface.end_game()
            machine_manager_service.stop_machine()
            
    
    def set_new_video(self, video: str):
        """Set new video """ 
        logger.info("Set new video")
        video_path = videos_list_manager_service.get_video_path(video)  
        if not video_path:
            logger.error("Video not found in config list")
            return False   
        self.video_capture_interface.set_video_to_play(video_path) 
        self.video = video
        self.reimaning_pitches = self.total_pitches
        return True
    
    def set_configuration(self, video: str, pitches: int):
        """Set configuration"""
        self.video_capture_interface.end_game()
        if not self.set_new_video(video):
            logger.error("Error in video setup")
            return None
        self.total_pitches = pitches
        
        return self.get_current_configuration()
    
    def get_current_configuration(self):
        """Get current video manager config"""
        return {"pitches": self.total_pitches, "video": self.video}
    
    def get_current_machine_status(self):
        """Get current machine status"""
        return {"running": self.video_capture_interface.running}


    def get_list_of_videos(self):
        """Get list of available videos"""
        #TODO: code

video_manager_service: VideoManager = VideoManager()
""" VideoManager  service singleton"""
