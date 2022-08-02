from .BaseEnv import BaseEnv

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
        """
        This is the funtion of screen cap 
        First you need to the below module before you run the code
        The code will keep capture the screen
        It can auto get the resolution of the screen
        Capture and return the screen in format of numpy.array
        And the frame-rate of screen capture better be more than 30 frames-per-second 
        """
        import cv2
        import mss
        import numpy
        import pyautogui

        with mss.mss() as sct:
            #It can get the size the screen and take the value for the resolution
            x,y=pyautogui.size()
            # The screen part to capture
            monitor = {"top": 0, "left": 0, "width": x, "height": y}

            while "Screen capturing":
              # Get raw pixels from the screen, save it to a Numpy array
              img = numpy.array(sct.grab(monitor))

              # Display the picture
              cv2.imshow("OpenCV/Numpy normal", img)

              # Display the picture in grayscale
              # cv2.imshow('OpenCV/Numpy grayscale',
              #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

              # print in 30 fps
              print("fps: {}".format(30))

              # Press "q" to quit
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
