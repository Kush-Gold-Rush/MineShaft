from .BaseEnv import BaseEnv
import time
import cv2
import mss
import numpy
from PIL import ImageGrab
import pyautogui

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=IO_MODE.FULL_CONTROL,
                 explore_space=EXPLORE_MODE.FULL):
        super(ThetanArenaEnv, self).__init__()
        
    def step(self, action):
        pass
    
    def reset(self):
        pass
    
    def close(self):
        pass
    
    def _take_action(self, action):
        pass
    
    def _screen_cap(self):
        """This is the function to capture screen from game in format of numpy.array.
        Screen resolution default set to screen resolution getting by pyautogui.size().
        
        """
        
        title = "FPS benchmark"
        start_time = time.time()
        display_time = 2
        fps = 0

        sct = mss.mss()
        x, y = pyautogui.size()
        monitor = {"top": 0, "left": 0, "width": x, "height": y}

        def screen_recordMSS():

            global fps, start_time
            while True:
                # Get raw pixels from the screen, save it to a Numpy array
                img = numpy.array(sct.grab(monitor))
                # to ger real color we do this:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                fps+=1
                TIME = time.time() - start_time
                if (TIME) >= display_time :
                    print("FPS: ", fps / (TIME))
                    fps = 0
                    start_time = time.time()

                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break
    
    def _keyboard_input(self, action):
        # scan and find keyboard action
        # key press # self._keyboard_press(ascii_list)
        # key release # self._keyboard_release(ascii_list)
        pass
    
    def _keyboard_press(self, ascii_list):
        pass

    def _keyboard_release(self, ascii_list):
        pass
    
    def _mouse_move(self, action):
        pass
    
    def _mouse_click(self, left, right):
        # scan and find mouse action
        # mouse press #self._mouse_press(left, right)
        # mouse release #self._mouse_release(left, right)
        pass
    
    def _mouse_press(self, left, right):
        pass
    
    def _mouse_release(self, left, right):
        pass
    
    def _start_game(self):
        pass
    
    def _end_game(self):
        pass
    
    def _reset_game(self):
        pass
