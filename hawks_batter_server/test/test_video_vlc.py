import vlc

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"


 
# creating vlc media player object
media = vlc.MediaPlayer(VIDEO_1)
 
# start playing video
media.play()