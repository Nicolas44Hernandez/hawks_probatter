import vlc
import time

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"
STARTUP_FRAME = "../../app_data/startup.png"

class VideoVLC():
    vlc_instance: vlc.Instance
    player: vlc
    media: vlc.Media
    video: str
    startup_frame: str
    playing_video: bool


    def __init__(self, video:str, startup_frame: str):  
        print("Video manager interface started") 
        print(f"Video: {video}")                 
                
        # Set initial values
        self.video = video
        self.startup_frame = startup_frame

        # creating a vlc instance
        self.vlc_instance = vlc.Instance() 
        # creating a media player
        self.player = self.vlc_instance.media_player_new()  
        self.player.video_set_scale(0.6) 

        self.load_video() 

        self.plot_startup_frame()

        # # Load video frames
        # if not self.load_video():
        #     return 
        
        # self.player.play()
        # time.sleep(0.4)
        # self.player.set_pause(1)

 
    def load_video(self):
        try:  
            # creating a media
            self.video_media = self.vlc_instance.media_new(self.video)
            self.video_media.add_option('start-time=0.5')     
            # setting media to the player
            self.player.set_media(self.video_media)   
            print("Video loaded") 
            return True 
        except:
            print("ERROR: error in video load")
            return False
    

    def load_startup_frame(self):        
    
        self.startup_media = self.vlc_instance.media_new(self.startup_frame)
        # setting media to the player
        self.player.set_media(self.startup_media)
        

        
    def run_video(self):
        if not self.playing_video:
            self.load_video()
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
        self.load_startup_frame()
        self.playing_video = False
        self.player.play() 
        
    

video_player = VideoVLC(VIDEO_1,STARTUP_FRAME)

while True: 
    for i in range(5):
        time.sleep(3)
        video_player.run_video()
        time.sleep(5)
        video_player.stop_video()
    video_player.plot_startup_frame()
    time.sleep(10)