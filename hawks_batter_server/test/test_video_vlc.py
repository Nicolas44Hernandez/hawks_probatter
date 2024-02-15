import vlc
import time

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"
STARTUP_FRAME = "../../app_data/startup.png"
SETUP_FRAME = "../../app_data/setup.jpg"

class VideoVLC():
    vlc_instance: vlc.Instance
    player: vlc
    video_media: vlc.Media
    setup_media: vlc.Media
    startup_media: vlc.Media
    video: str
    startup_frame: str
    setup_frame: str
    playing_video: bool


    def __init__(self, video:str, startup_frame: str, setup_frame: str):  
        print("Video manager interface started") 
        print(f"Video: {video}")                 
                
        # Set initial values
        self.video = video
        self.startup_frame = startup_frame
        self.setup_frame = setup_frame

        # creating a vlc instance
        self.vlc_instance = vlc.Instance() 
        # creating a media player
        self.player = self.vlc_instance.media_player_new()  
        self.player.video_set_scale(0.6) 

        self.load_video() 
        self.load_startup_frame()
        self.load_setup_frame()

        self.plot_startup_frame()

 
    def load_video(self):
        try:  
            # creating a media
            self.video_media = self.vlc_instance.media_new(self.video)
            self.video_media.add_option('start-time=0.5')     
            # setting media to the player
            print("Video loaded") 
            return True 
        except:
            print("ERROR: error in video load")
            return False
    

    def load_startup_frame(self):   
        print("Loadding startup image")    
        self.startup_media = self.vlc_instance.media_new(self.startup_frame) 
    
    def load_setup_frame(self):   
        print("Loadding startup image")    
        self.setup_media = self.vlc_instance.media_new(self.setup_frame) 

        
    def run_video(self):
        if not self.playing_video:
            self.player.set_media(self.video_media)   
            self.player.play()
        self.playing_video = True
        self.player.set_time(0)
        self.player.set_pause(0)
        

    def stop_video(self):
        if self.playing_video:
            self.player.set_time(0)
            time.sleep(0.4)
            self.player.set_pause(1)  

    def plot_startup_frame(self):
        self.player.set_media(self.startup_media)   
        self.playing_video = False
        self.player.play()
    
    def plot_waiting_for_pitch(self):
        if not self.playing_video:
            self.player.set_media(self.video_media)   
            self.player.play()
        self.player.set_time(0)
        time.sleep(0.5)
        self.player.set_pause(1)  
        
    
    def plot_setup_frame(self):
        self.player.set_media(self.setup_media)   
        self.playing_video = False
        self.player.play()

    def set_video(self, video:str):
        self.video = video
        self.load_video()
        
    

video_player = VideoVLC(VIDEO_1,STARTUP_FRAME, SETUP_FRAME)

while True: 
    time.sleep(3)
    video_player.plot_setup_frame() 
    time.sleep(3)  
    for i in range(2):
        video_player.plot_waiting_for_pitch()
        time.sleep(3)
        video_player.run_video()
        time.sleep(5)
        video_player.plot_waiting_for_pitch()

    time.sleep(10)
    video_player.set_video(VIDEO_2)