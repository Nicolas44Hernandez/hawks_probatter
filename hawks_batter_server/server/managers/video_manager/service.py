"""
Video manager service
"""
import logging
import time
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
    on_game: bool
    

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
            self.on_game = False

            logger.info(f"Default number of pitches: {self.total_pitches}")            

            self.keboard_input_interface = KeyboardInputInterface(
                setup_callback=self.setup_image, 
                run_callback=self.new_game, 
                exit_callback=self.exit_game, 
                start_pitch_callback=self.start_pitch, 
                end_pitch_callback=self.end_pitch, 
            )

            self.video_capture_interface = VideoCaptureInterface(
                video=videos_list_manager_service.get_video_path(self.video), 
                setup_frame=app.config["SETUP_FRAME"],
                startup_frame=app.config["STARTUP_FRAME"],
            )

            self.video_capture_interface.start()
        
    def start_pitch(self):
        #logger.info("Start pitch callback")   
        if not self.on_game: 
            self.new_game()    
        if self.video_capture_interface.running and self.video_capture_interface.waiting_for_start:
            logger.info("START PITCH")          
            self.video_capture_interface.run_video()        
    
    def end_pitch(self):
        #logger.info("end pitch callback")   
        if self.on_game:     
            logger.info("END PITCH")
            # Wait the end and stop video
            time.sleep(1.5)        
            self.reimaning_pitches = self.reimaning_pitches - 1 
            logger.info(f"Remaining pitches: {self.reimaning_pitches}")
            if self.reimaning_pitches <= 0:
                    logger.info("Game is over. Restar from website or manually")
                    machine_manager_service.stop_machine()
                    self.exit_game()
            else:
                logger.info("Plotting waiting for pitch")
                self.video_capture_interface.plot_waiting_for_pitch()
                    
    def setup_image(self):
        """Setup image"""
        machine_manager_service.stop_machine()
        self.video_capture_interface.setup()    
        self.on_game=False    

    def new_game(self):
        """New game"""
        if self.video_capture_interface.setting_up:
            logger.error("Imposible to run new game, setting up")
            return 
        logger.info("Starting new game")
        self.reimaning_pitches = self.total_pitches
        machine_manager_service.stop_machine()
        self.video_capture_interface.plot_waiting_for_pitch()
        machine_manager_service.start_machine()
        self.on_game=True

    def exit_game(self):
        """Exit game """       
        machine_manager_service.stop_machine()
        self.video_capture_interface.plot_startup_frame()
        self.on_game=False          
    
    def set_new_video(self, video: str):
        """Set new video """ 
        logger.info(f"Setting new video: {video}")
        video_path = videos_list_manager_service.get_video_path(video)  
        logger.info(f"video_path: {video_path}")
        if not video_path:
            logger.error("Video not found in config list")
            return False   
        self.video_capture_interface.set_video(video_path) 
        self.video = video
        self.reimaning_pitches = self.total_pitches
        return True
    
    def set_configuration(self, video: str, pitches: int):
        """Set configuration"""
        logger.info(f"Setting configuration video: {video} pitches: {pitches}")
        self.exit_game()
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
        return {"running": self.on_game}

    def get_list_of_videos(self):
        """Get list of available videos"""
        #TODO: code

video_manager_service: VideoManager = VideoManager()
""" VideoManager  service singleton"""
