"""
KeyboardInputInterface interface service
"""
import logging
import threading
import cv2

interframe_wait_ms = 30

logger = logging.getLogger(__name__)

class KeyboardInputInterface(threading.Thread):
    """Service class for keyboard input management"""
  
    setup_callback: callable
    run_callback: callable
    exit_callback: callable
    new_video_callback: callable

    def __init__(
            self,
            setup_callback: callable,
            run_callback: callable, 
            exit_callback: callable, 
            new_video_callback: callable 
        ):  
        logger.info("Keyboard input interface started")        

        # init values
        self.setup_callback= setup_callback
        self.run_callback=run_callback
        self.exit_callback=exit_callback
        self.new_video_callback=new_video_callback

        # Call Super constructor
        super(KeyboardInputInterface, self).__init__(name="KeyboardInputInterfaceThread")
        self.setDaemon(True)

    def run(self):
        """Run thread"""      
        
        while True:      
            pressed_key =  cv2.waitKey(interframe_wait_ms)
            if pressed_key:
                if pressed_key == ord('c'):
                    self.setup_callback()
                elif pressed_key == ord('r'):
                    self.run_callback()
                elif pressed_key == ord('q'):
                    self.exit_callback()
                elif pressed_key == ord('n'):
                    self.new_video_callback()
        