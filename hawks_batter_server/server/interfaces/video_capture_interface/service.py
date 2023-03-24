"""
Video capture interface service
"""
import logging
import threading
import cv2
import numpy


WINDOW_NAME = "HAWKS BASEBALL"
interframe_wait_ms = 30

PICTURE_RATIO = 0.8

logger = logging.getLogger(__name__)

class VideoCaptureInterface(threading.Thread):
    """Service class for video manager interface management"""

    capture: cv2.VideoCapture
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
        if not captured_setup_frame: 
            logger.error("Impossible to open setup frame")
            return 
        self.setup_frame = captured_setup_frame

        # Load startup frame
        captured_startup_frame = self.load_image(startup_frame)
        if not captured_setup_frame: 
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
        else: 
            logger.error("Impossible to open video")
            return

        # Running flag
        

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
                self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                cv2.imshow(WINDOW_NAME, self.setup_frame) 
                continue   
            if not self.running:
                cv2.imshow(WINDOW_NAME, self.setup_frame)  
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
            
            pressed_key =  cv2.waitKey(interframe_wait_ms)
            if pressed_key:
                if pressed_key == ord('c'):
                    if not self.setting_up:
                        self.set_up_image_video(True)
                    else:
                        self.set_up_image_video(False)
                elif pressed_key == ord('r'):
                    if not self.running:
                        self.set_up_image_video(True)
                    else:
                        self.set_up_image_video(False)
                elif pressed_key == ord('q'):
                    logger.info("Exit requested.")
                    break       

        logger.info("End of VideoCapture Thread")
        self.capture.release()
        cv2.destroyAllWindows()

    def start_game(self):
        """Start game"""
        logger.info("starting game")
        self.running = True
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

    def stop_video(self):
        """Stop video"""
        self.waiting_for_start = True
        logger.info("Stop video")
    
    def set_up_image_video(self, setup: bool=True):
        """Show setup image"""
        #TODO: stop machine
        self.setting_up = setup
        self.running = False
    
    def load_image(self, path_to_frame: str)-> numpy.ndarray:
        """Load a frame"""
        # Get frame
        cap = cv2.VideoCapture(path_to_frame)
        ret, frame = cap.read()
        if not ret:
            frame = False
            logger.error("Impossible to open setup frame")
        cap.release()
        return frame
