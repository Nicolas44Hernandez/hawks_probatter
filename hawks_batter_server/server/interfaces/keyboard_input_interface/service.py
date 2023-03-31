"""
KeyboardInputInterface interface service
"""
import logging
import threading
import cv2
from pynput import keyboard 

waiting_ms = 100

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

        # Start keyboard listener          
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

            # keyboard.on_press_key("c", lambda _:self.setup_image())
            # keyboard.on_press_key("r", lambda _:self.new_game())
            # keyboard.on_press_key("q", lambda _:self.exit_game())
            # keyboard.on_press_key("n", lambda _:self.set_new_video())

        # # Call Super constructor
        # super(KeyboardInputInterface, self).__init__(name="KeyboardInputInterfaceThread")
        # self.setDaemon(True)

    def on_press(self, key):
        """Callback for key pressed"""
        logger.info(f"key pressed {key}")
        # try:
        #     print('alphanumeric key {0} pressed'.format(
        #         key.char))
        # except AttributeError:
        #     print('special key {0} pressed'.format(
        #         key))

    # def run(self):
    #     """Run thread"""   
    #     while True:      
    #         logger.info("Loop")
    #         try:  
    #             if keyboard.is_pressed('c'):  
    #                 self.setup_callback()
    #                 continue 
    #             if keyboard.is_pressed('r'):  
    #                 self.run_callback()
    #                 continue 
    #             if keyboard.is_pressed('q'):  
    #                 self.exit_callback()
    #                 continue 
    #             if keyboard.is_pressed('n'):  
    #                 self.new_video_callback()
    #                 continue 
    #         except:
    #             logger.info("Exception")
    #             continue  
    #         # pressed_key =  cv2.waitKey(waiting_ms)
    #         # if pressed_key:
    #         #     if pressed_key == ord('c'):
    #         #         self.setup_callback()
    #         #     elif pressed_key == ord('r'):
    #         #         self.run_callback()
    #         #     elif pressed_key == ord('q'):
    #         #         self.exit_callback()
    #         #     elif pressed_key == ord('n'):
    #         #         self.new_video_callback()
        

    
    