import vlc
import time

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"


 
 
 
# method to play video
def video(source):
     
    # creating a vlc instance
    vlc_instance = vlc.Instance()
     
    # creating a media player
    player = vlc_instance.media_player_new()
     
    # creating a media
    media = vlc_instance.media_new(source)
     
    # setting media to the player
    player.set_media(media)   
    
    
    # play the video
    player.play()
    
    time.sleep(2)
    
    
    # pause video
    player.set_pause(1)


    player.set_time(0) # start at 1 seconds

    time.sleep(2)

     
    # getting the duration of the video
    duration = player.get_length()
     
    # printing the duration of the video
    print("Duration : " + str(duration))
     
# call the video method
video(VIDEO_1)

while True: 
    a = 4