"""
Video capture interface service
"""
import logging
import threading
import cv2
import numpy
import os
import time

WINDOW_NAME = "HAWKS BASEBALL"

logger = logging.getLogger(__name__)

class VideoCaptureInterface(threading.Thread):
    """Service class for video manager interface management"""

    capture: cv2.VideoCapture
    fps: int
    running: bool
    setting_up: bool
    waiting_for_start: bool
    waiting_for_pitch_frame: numpy.ndarray
    startup_frame: numpy.ndarray
    setup_frame: numpy.ndarray    

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
        self.running = False
        self.setting_up = False
        self.waiting_for_start = True   
        self.capture = cv2.VideoCapture(video)

        # Get first frame
        ret, frame = self.capture.read()
        if ret:
            self.waiting_for_pitch_frame = frame
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        else: 
            logger.error("Impossible to open video")
            return        
        logger.info(f"Playing video {video} fps:{self.fps}")

        # Call Super constructor
        super(VideoCaptureInterface, self).__init__(name="VideoCaptureInterfaceThread")
        self.setDaemon(True)

    def run(self):
        """Run thread"""      
        #cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:   
            if self.setting_up:
                self.running = False
                self.waiting_for_start = True  
                cv2.imshow(WINDOW_NAME, self.setup_frame)             
            else:   
                if not self.running:
                    cv2.imshow(WINDOW_NAME, self.startup_frame)  
                    self.waiting_for_start = True
                else:
                    if not self.waiting_for_start:                  
                        ret, frame = self.capture.read()
                        if not ret:
                            logger.info("Reached end of video")
                            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                            self.waiting_for_start = True
                            continue  
                        cv2.imshow(WINDOW_NAME, frame)
                    else:                    
                        self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        cv2.imshow(WINDOW_NAME, self.waiting_for_pitch_frame)
            cv2.waitKey(30)
            # pressed_key =  cv2.waitKey(interframe_wait_ms)
            # if pressed_key:
            #     if pressed_key == ord('c'):
            #         logger.info("Key c pressed")
            #         if not self.setting_up:
            #             self.set_up_image(True)
            #         else:
            #             self.set_up_image(False)
            #     elif pressed_key == ord('r'):
            #         logger.info("Key r pressed")
            #         if not self.running:
            #             self.start_game()
            #         else:
            #             self.end_game()
            #     elif pressed_key == ord('q'):
            #         logger.info("Key q pressed")
            #         logger.info("Exit requested.")
            #         break
            #     elif pressed_key == ord('n'):
            #         logger.info("Key n pressed")
            #         self.set_video_to_play("/home/pi/workspace/hawks_probatter/app_data/videos/v2.mp4") 

        logger.info("End of VideoCapture Thread")
        self.capture.release()
        cv2.destroyAllWindows()

    def start_game(self):
        """Start game"""
        logger.info("starting game")
        self.running = True
        self.setting_up=False
        self.waiting_for_start = True
    
    def end_game(self):
        """End game"""
        logger.info("Ending game")
        self.running = False
        self.waiting_for_start = True

    def run_video(self, remaining_pitches: int):
        """Launch video"""      
        self.waiting_for_start = False
        logger.info(f"Running video, remaining pitches {remaining_pitches}")
        # TODO: modify watting frame to show remaining pitches

    def set_video_to_play(self, video: str):
        """Set a new video to play"""
        # Check if file exists 
        if not os.path.exists(video): 
            logger.error(f"Video {video} doesnt exist")
            return False
        self.stop_video()
        self.running = False
        self.capture.release()
        time.sleep(2)
        self.capture = cv2.VideoCapture(video)
         # Get first frame
        ret, frame = self.capture.read()
        if ret:
            self.waiting_for_pitch_frame = frame
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)            
        else: 
            logger.error("Impossible to open video")
            return False  
        logger.info(f"Playing video {video} fps:{self.fps}")
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
