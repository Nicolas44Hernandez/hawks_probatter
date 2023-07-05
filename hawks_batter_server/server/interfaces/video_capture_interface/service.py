"""
Video capture interface service
"""
import logging
import threading
from typing import Iterable
import cv2
import numpy
import os
import time

WINDOW_NAME = "HAWKS BASEBALL"

logger = logging.getLogger(__name__)

class VideoCaptureInterface(threading.Thread):
    """Service class for video manager interface management"""

    video: str
    interframe_time: int
    running: bool
    setting_up: bool
    waiting_for_start: bool
    waiting_for_pitch_frame: numpy.ndarray
    startup_frame: numpy.ndarray
    setup_frame: numpy.ndarray    
    video_frames: Iterable[numpy.ndarray]
    remaining_pitches: int

    def __init__(self, video:str, setup_frame: numpy.ndarray, startup_frame: numpy.ndarray):  
        logger.info("Video manager interface started") 
        logger.info(f"Default video: {video}")            

        # Load setup frame
        captured_setup_frame = self.load_image(setup_frame)
        if captured_setup_frame is None: 
            logger.error("Impossible to open setup frame")
            return 
        self.setup_frame = captured_setup_frame

        # Load startup frame
        captured_startup_frame = self.load_image(startup_frame)
        if captured_startup_frame is None: 
            logger.error("Impossible to open startup frame")
            return 
        self.startup_frame = captured_startup_frame        
                
        # Set initial values
        self.video = video
        self.running = False
        self.setting_up = False
        self.waiting_for_start = True  
        self.interframe_time = None 
        self.remaining_pitches = None

        # Load video frames
        self.video_frames = None
        self.video_frames = self.load_video(video)
        if self.video_frames is None:
            logger.error("Impossible to open video")
            return 
        
        # Get first frame 
        self.waiting_for_pitch_frame = self.video_frames[0]

        # Call Super constructor
        super(VideoCaptureInterface, self).__init__(name="VideoCaptureInterfaceThread")
        self.setDaemon(True)

    def draw_text(self, frame, text, font=cv2.FONT_HERSHEY_DUPLEX, pos=(20, 100), font_scale=3, font_thickness=5, text_color=(77, 8, 7),text_color_bg=(255, 255, 255)):
            
        """Draw text in frame"""
        x, y = pos
        text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_w, text_h = text_size
        cv2.rectangle(frame, pos, (x + text_w + 5, y + text_h + 5), text_color_bg, -1)
        cv2.putText(frame, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)
        return text_size

    def run(self):
        """Run thread"""      
        time.sleep(5)
        cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        current_frame_pos = 0 
        while True:   
            if self.setting_up:
                self.running = False
                self.waiting_for_start = True  
                cv2.imshow(WINDOW_NAME, self.setup_frame) 
                current_frame_pos = 0            
            else:   
                if not self.running:
                    cv2.imshow(WINDOW_NAME, self.startup_frame)  
                    self.waiting_for_start = True
                    current_frame_pos = 0 
                else:
                    if not self.waiting_for_start:   
                        current_frame_pos = current_frame_pos + 1
                        if current_frame_pos > len(self.video_frames) - 1 :
                            self.waiting_for_start = True
                            continue
                        raw_frame = self.video_frames[current_frame_pos]  
                        frame = raw_frame.copy()                                              
                        #logger.info(f"frame {current_frame_pos}")
                        if self.remaining_pitches is not None:                            
                            text = f"P:{self.remaining_pitches}"
                            self.draw_text(frame, text)
                        cv2.imshow(WINDOW_NAME, frame)
                    else:
                        raw_frame = self.waiting_for_pitch_frame 
                        frame = raw_frame.copy() 
                        if self.remaining_pitches is not None:                              
                            text = f"P:{self.remaining_pitches}"  
                            self.draw_text(frame, text)                                     
                        cv2.imshow(WINDOW_NAME, frame)
                        current_frame_pos = 0 
            cv2.waitKey(int(self.interframe_time/2))

    def start_game(self):
        """Start game"""
        logger.info("starting game")
        self.running = True
        self.setting_up=False
        self.waiting_for_start = True
    
    def end_game(self, remaining_pitches):
        """End game"""
        logger.info("Ending game")
        self.remaining_pitches = remaining_pitches
        self.running = False
        self.waiting_for_start = True

    def run_video(self, remaining_pitches: int):
        """Launch video"""      
        self.waiting_for_start = False
        self.remaining_pitches = remaining_pitches
        logger.info(f"Running video, remaining pitches {remaining_pitches}")
        

    def set_video_to_play(self, video: str):
        """Set a new video to play"""
        # Check if file exists 
        if not os.path.exists(video): 
            logger.error(f"Video {video} doesnt exist")
            return False
        self.stop_video()
        self.running = False

        # Load video frames
        self.video_frames = None
        self.video_frames = self.load_video(video)
        if self.video_frames is None:
            logger.error("Impossible to open video")
            return False
        
        # Get first frame 
        self.waiting_for_pitch_frame = self.video_frames[0]
        return True    

    def stop_video(self):
        """Stop video"""
        self.waiting_for_start = True
        logger.info("Stop video")
    
    def set_up_image(self, setup: bool=True):
        """Show setup image"""
        #TODO: stop machine
        logger.info(f"Setting up {setup}")
        self.setting_up = setup
        self.running = setup
    
    def load_image(self, path_to_frame: str)-> numpy.ndarray:
        """Load a frame"""
        # Get frame
        cap = cv2.VideoCapture(path_to_frame)
        ret, frame = cap.read()
        if not ret:
            frame = None
            logger.error("Impossible to open setup frame")
        cap.release()
        return frame

    def load_video(self, video: str):
        """Load video in array"""

        logger.info(f"Loading video: {video}")

        cap = cv2.VideoCapture(video)
        fps = cap.get(cv2.CAP_PROP_FPS) 
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        interframe_time = int(1000/fps)

        logger.info(f"Video fps: {fps}")
        logger.info(f"Total frames: {total}")
        logger.info(f"Interframe time: {interframe_time}")

        video_frames = []

        # Check if video opened successfully
        if (cap.isOpened()== False):
            logger.info("Error opening video file")
            return None
        
        # Read until video is complete
        while(cap.isOpened()):      
            ret, frame = cap.read()
            if ret == True:
                video_frames.append(frame)  
            else:
                break
        
        cap.release()
        logger.info(f"Total frames in video: {len(video_frames)}")
        self.interframe_time = interframe_time
        return video_frames                