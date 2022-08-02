from .BaseEnv import BaseEnv

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=BaseEnv.IO_MODE.FULL_CONTROL,
                 explore_space=BaseEnv.EXPLORE_MODE.FULL):
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
        pass
    
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
        """
        This is the code of start game
        
        "import os"
        
        First it need to import the os for use the software
        
        "os.startfile("C:\Program Files (x86)\Thetan Arena\Thetan Arena.exe")" This is the hardcode path to open the game
        """
        import os
        
        os.startfile("C:\Program Files (x86)\Thetan Arena\Thetan Arena.exe")
        
        """
        This is the code of open Enter Tutorial of Deathmatch by hardcode the mouse location
        This code only work on pc with the screen resolution is 1980 x 1080
        The code need to run after enter the game of TheTan Arena
        """
        
        pyautogui.moveTo(1347,989,1) 
        pyautogui.leftClick()
        time.sleep(2)
        
        pyautogui.dragTo(300, 400, 2, button='left')
        time.sleep(2)
        
        pyautogui.moveTo(1451,317,2)
        pyautogui.leftClick()
        time.sleep(2)
        
        pyautogui.moveTo(948,754,2) 
        pyautogui.leftClick()
        
    
    def _end_game(self):
        pass
    
    def _reset_game(self):
        pass
