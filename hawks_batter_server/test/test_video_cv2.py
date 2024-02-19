# importing libraries 
import cv2 
import numpy as np 

VIDEO_1 = "../../app_data/videos/jules_windup.mp4"
VIDEO_2 = "../../app_data/videos/jules_slide_step.mp4"
STARTUP_FRAME = "../../app_data/startup.png"
SETUP_FRAME = "../../app_data/setup.jpg"

  
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(VIDEO_1) 
  
# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 
else:
    print("file opened")
  
# Read until video is completed 
while(cap.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True: 
    # Display the resulting frame 
        cv2.imshow('Frame', frame) 
          
    # Press Q on keyboard to exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
cap.release() 
  
# Closes all the frames 
cv2.destroyAllWindows() 