"""
Video capture interface service
"""
import threading
from typing import Iterable
import cv2
import numpy
import os
import time

WINDOW_NAME = "VIDEO TEST HAWKS BASEBALL"
VIDEO_TO_PLAY = "/home/pi/hawks_probatter/app_data/videos/jules_windup.mp4"


class VideoCaptureInterface(threading.Thread):
    """Service class for video manager interface management"""

    video: str
    video_frames: Iterable[numpy.ndarray]

    def __init__(self, video:str):  
        print("Video manager interface started") 
        print(f"Video: {video}")                 
                
        # Set initial values
        self.video = video

        # Load video frames
        self.video_frames = None
        self.video_frames = self.load_video(video)
        if self.video_frames is None:
            print("ERROR: Impossible to open video")
            return 
        
        # Get first frame 
        self.waiting_for_pitch_frame = self.video_frames[0]

        # Call Super constructor
        super(VideoCaptureInterface, self).__init__(name="VideoCaptureInterfaceThread")
        self.setDaemon(True)

    def run(self):
        """Run thread"""      
        time.sleep(5)
        # cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        current_frame_pos = 0 
        while True:                
            current_frame_pos = current_frame_pos + 1
            if current_frame_pos > len(self.video_frames) - 1 :
                return
            raw_frame = self.video_frames[current_frame_pos]  
            frame = raw_frame.copy()                                              
            print(f"frame {current_frame_pos}")
            cv2.imshow(WINDOW_NAME, frame)
            cv2.waitKey(8)

    def load_video(self, video: str):
        """Load video in array"""

        print(f"Loading video: {video}")

        cap = cv2.VideoCapture(video)
        fps = cap.get(cv2.CAP_PROP_FPS) 
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        print(f"Video fps: {fps}")
        print(f"Total frames: {total}")

        video_frames = []

        # Check if video opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            return None
        
        # Read until video is complete
        while(cap.isOpened()):      
            ret, frame = cap.read()
            if ret == True:
                video_frames.append(frame)  
            else:
                break
        
        cap.release()
        print(f"Total frames in video: {len(video_frames)}")
        return video_frames                
    

def check_video_file(video: str):
    """Check if video file exists"""
    file_exists = os.path.isfile(video)
    if not file_exists:
        print(f"ERROR: video file {video} doesnt exists")
    return file_exists
 
def run_video(video: str):
    video_capture_interface = VideoCaptureInterface(video=video)
    video_capture_interface.run()

if __name__ == '__main__':
    if check_video_file(video=VIDEO_TO_PLAY):
        run_video(video=VIDEO_TO_PLAY)