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
    setup_frame: numpy.ndarray

    def __init__(self, video:str, setup_frame: str):  
        logger.info(f"Default video: {video}")
        logger.info("Video manager interface started")        

        # Get Setup frame frame
        cap = cv2.VideoCapture(setup_frame)
        ret, frame = cap.read()
        if ret:
            self.setup_frame = frame
        else: 
            logger.error("Impossible to open setup frame")
            return        
        cap.release()

        self.setting_up = True
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
        self.running = True

        # Call Super constructor
        super(VideoCaptureInterface, self).__init__(name="VideoCaptureInterfaceThread")
        self.setDaemon(True)

    def run(self):
        """Run thread"""      
        #cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while self.running:      
            if not self.waiting_for_start:                  
                ret, frame = self.capture.read()
                if not ret:
                    logger.info("Reached end of video")
                    self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    self.waiting_for_start = True  
                cv2.imshow(WINDOW_NAME, frame)
            else:
                if self.setting_up:
                    self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    cv2.imshow(WINDOW_NAME, self.setup_frame)                
                else:
                    self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    cv2.imshow(WINDOW_NAME, self.waiting_for_pitch_frame)
            
            if cv2.waitKey(interframe_wait_ms):
                if 0x7F == ord('q'):
                    logger.info("Exit requested.")
                    break
            
            if cv2.waitKey(interframe_wait_ms):
                if 0x7F == ord('c'):
                    if not self.setting_up:
                        self.set_up_image_video(True)
                    else:
                        self.set_up_image_video(False)

                    

                         
        logger.info("End of VideoCapture Thread")
        self.capture.release()
        cv2.destroyAllWindows()

    def run_video(self):
        """Launch video"""
        self.waiting_for_start = False
        logger.info("Running video")

    def stop_video(self):
        """Stop video"""
        self.waiting_for_start = True
        logger.info("Stop video")
    
    def set_up_image_video(self, setup: bool=True):
        """Show setup image"""
        self.setting_up = setup
        self.waiting_for_start = True
        
