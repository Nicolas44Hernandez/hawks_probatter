"""
KeyboardInputInterface interface service
"""
import logging
import threading
import cv2
import sys
import select
import time

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
            input = select.select([sys.stdin], [], [], 1)[0]
            if input:
                pressed_key = sys.stdin.readline().rstrip()
                logger.info(f"pressed key {pressed_key}")
        
                # if (pressed_key == "q"):
                #     print "Exiting"
                #     sys.exit(0)
                # else:
                #     print "You entered: %s" % value
            else:
                logger.info("noting pressed")
                time.sleep(0.2)

            # pressed_key =  cv2.waitKey(interframe_wait_ms)
            # if pressed_key:
            #     if pressed_key == ord('c'):
            #         self.setup_callback()
            #     elif pressed_key == ord('r'):
            #         self.run_callback()
            #     elif pressed_key == ord('q'):
            #         self.exit_callback()
            #     elif pressed_key == ord('n'):
            #         self.new_video_callback()
        