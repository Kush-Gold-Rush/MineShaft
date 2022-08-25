import pyautogui
import time
""" 
Parameters
----------
value: float
    positive or negative parameter value of the distance of mouse scroll

scroll_step: float
    times of loop

    Scroll up as positive parameter value and down as negative parameter value
    Value parameter times in self.scroll_step, in __init__(self, value, scroll_step)
    Using pyautogui.scroll() to do the action of mouse_scroll_function
    The move of mouse always be done within 0.2 second by using time.sleep(0.2)

Returns
-------
scroll_step: float
    the total looping time
"""

class mouse_scroll_function:

    def __init__(self,value,scroll_step):
        self.value = value
        self.scroll_step = scroll_step

    def _mouse_scroll(self,value, scroll_step):
        for num in range(scroll_step):
                pyautogui.scroll(value)
                time.sleep(0.2)


    def _scroll_step(self):
        return self.scroll_step