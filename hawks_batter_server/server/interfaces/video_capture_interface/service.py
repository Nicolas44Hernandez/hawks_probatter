"""
Video capture interface service
"""
import logging
import vlc
import os
import time

WINDOW_NAME = "HAWKS BASEBALL"

logger = logging.getLogger(__name__)

class VideoCaptureInterface():
    """Service class for video manager interface management"""

    vlc_instance: vlc.Instance
    player: vlc
    video_media: vlc.Media
    setup_media: vlc.Media
    startup_media: vlc.Media
    video: str
    startup_frame: str
    setup_frame: str
    waiting_for_start: bool
    remaining_pitches: int
    setting_up: bool
    running: bool

    def __init__(self, video:str, setup_frame: str, startup_frame: str):  
        logger.info("Video manager interface started") 
        logger.info(f"Default video: {video}")   

        # Set initial values
        self.video = video
        self.startup_frame = startup_frame
        self.setup_frame = setup_frame   
        self.setting_up = False
        self.running = False
        self.remaining_pitches = None 

        # creating a vlc instance
        self.vlc_instance = vlc.Instance() 
        # creating a media player
        self.player = self.vlc_instance.media_player_new()  
        self.player.video_set_scale(0.6)      

        # Load video
        if not self.load_video():
            return False

        # Load setup frame
        self.load_setup_frame()       

        # Load startup frame
        self.load_startup_frame()      

        # Plot startup frame
        self.plot_startup_frame()

    # def draw_text(self, frame, text, font=cv2.FONT_HERSHEY_DUPLEX, pos=(20, 100), font_scale=3, font_thickness=5, text_color=(77, 8, 7),text_color_bg=(255, 255, 255)):
            
    #     """Draw text in frame"""
    #     x, y = pos
    #     text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    #     text_w, text_h = text_size
    #     cv2.rectangle(frame, pos, (x + text_w + 5, y + text_h + 5), text_color_bg, -1)
    #     cv2.putText(frame, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)
    #     return text_size


    def load_video(self):
        try:  
            # Check if file exists 
            if not os.path.exists(self.video): 
                logger.error(f"Video {self.video} doesnt exist")
                return False       

            # creating a media
            self.video_media = self.vlc_instance.media_new(self.video)
            self.video_media.add_option('start-time=0.5')     
            # setting media to the player
            logger.info("Video loaded") 
            return True 
        except:
            logger.error("ERROR: error in video load")
            return False               

    def set_video(self, video:str):
        """Set video to play"""
        
        # Check if file exists 
        if not os.path.exists(video): 
            logger.error(f"Video {video} doesnt exist")
            return False
        
        # plot startup frame
        self.running = False
        self.plot_startup_frame()       

        self.video = video        
        if not self.load_video():
            return False
        return True

    def load_startup_frame(self):   
        print("Loadding startup image")    
        self.startup_media = self.vlc_instance.media_new(self.startup_frame) 
    
    def load_setup_frame(self):   
        print("Loadding startup image")    
        self.setup_media = self.vlc_instance.media_new(self.setup_frame) 

    def run_video(self):
        if not self.running:
            self.player.set_media(self.video_media)   
            self.player.play()
        self.running = True
        self.player.set_time(0)
        self.player.set_pause(0)    
    
    def plot_startup_frame(self):
        self.running = False
        self.setting_up = False
        self.player.set_media(self.startup_media)   
        self.player.play()
    
    def plot_waiting_for_pitch(self):
        if not self.running or not self.player.is_playing():
            self.player.set_media(self.video_media)   
            self.player.play()
        self.player.set_time(0)
        time.sleep(0.5)
        self.player.set_pause(1)  
        self.running = False
        
    def plot_setup_frame(self):
        self.player.set_media(self.setup_media)  
        self.setting_up = True 
        self.running = False
        self.player.play()
    
    def setup(self):
        """Show setup frame"""
        if not self.setting_up:
            self.plot_setup_frame()
            logger.info(f"Setting up image")
        else: 
            self.plot_startup_frame()
            self.setting_up = False 
            logger.info(f"Settup done") 