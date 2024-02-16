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
    start_pitch_callback: callable
    end_pitch_callback: callable

    def __init__(
            self,
            setup_callback: callable,
            run_callback: callable, 
            exit_callback: callable, 
            start_pitch_callback: callable,
            end_pitch_callback: callable,
        ):  
        logger.info("Keyboard input interface started")        

        # init values
        self.setup_callback= setup_callback
        self.run_callback=run_callback
        self.exit_callback=exit_callback
        self.start_pitch_callback=start_pitch_callback
        self.end_pitch_callback=end_pitch_callback

        # Start keyboard listener          
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()       
    def on_press(self, key):
        """Callback for key pressed""" 
        try:       
            pressed_key = key.char
        except:
            return
        if pressed_key == 'c' :  
            self.setup_callback()
            return
        if pressed_key == 'r':  
            self.run_callback()
            return
        if pressed_key == 'q':  
            self.exit_callback()
            return
        if pressed_key == 'p':  
            self.start_pitch_callback()
            return
        if pressed_key == 's':  
            self.end_pitch_callback()
            return

  
    
    