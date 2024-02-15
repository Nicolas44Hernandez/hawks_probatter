import vlc
import time

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"

class VideoVLC():
    vlc_instance: vlc.Instance
    player: vlc
    media: vlc.Media


    def __init__(self, video:str):  
        print("Video manager interface started") 
        print(f"Video: {video}")                 
                
        # Set initial values
        self.video = video

        # Load video frames
        if not self.load_video():
            return 
        
        # plot first frame
        self.player.play()
        time.sleep(0.5)
        self.player.set_pause(1)

 
    def load_video(self):
        try:
            # creating a vlc instance
            self.vlc_instance = vlc.Instance()     
            # creating a media player
            self.player = self.vlc_instance.media_player_new()     
            # creating a media
            self.media = self.vlc_instance.media_new(self.video)     
            # setting media to the player
            self.player.set_media(self.media)   
            print("Video loaded") 
            return True 
        except:
            print("ERROR: error in video load")
            return False
    
    def plot_first_frame(self):
        # plot first frame
        self.player.play()
        time.sleep(0.5)
        self.player.set_pause(1)
        
    def run_video(self):
        self.player.set_pause(0)

    def stop_video(self):
        self.player.stop()
        self.plot_first_frame()
        
    

video_player = VideoVLC(VIDEO_1)

while True: 
    time.sleep(5)
    video_player.run_video()
    time.sleep(3)
    video_player.stop_video()