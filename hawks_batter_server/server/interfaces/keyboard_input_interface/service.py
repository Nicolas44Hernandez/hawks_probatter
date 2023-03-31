"""
KeyboardInputInterface interface service
"""
import logging
import threading
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
    def on_press(self, key):
        """Callback for key pressed"""
        logger.info(f"key pressed {key}")
        key = f"key"
        if key =='c':  
            self.setup_callback()
            return
        if key =='r':  
            self.run_callback()
            return
        if key =='q':  
            self.exit_callback()
            return
        if key =='n':  
            self.new_video_callback()
            return

  
    
    