
import os
import numpy as np
import cv2 as cv

import pyautogui as py
import win32gui
import win32ui
import win32con
from threading import Thread, Lock
import pygetwindow as gw
import mss
import d3dshot
from time import time


class WindowCapture():
    # class properties

    hwnd = None
    d = None

    def __init__(self):
        '''
        initialize the d3dshot object 
        '''
        self.hwnd = win32gui.GetDesktopWindow()
        self.d = d3dshot.create(capture_output='numpy')

    def get_screenshot(self):
        loop_time = time()
        windows_list = []
        toplist = []
        '''
        locate the game window position
        '''
        with mss.mss() as sct:
            gameWindow = gw.getWindowsWithTitle('Thetan Arena')[0]
            monitor =  (gameWindow.top,
                       gameWindow.left,
                       gameWindow.width,
                       gameWindow.height)
        
        top, left, width, height = monitor
        '''
        take the screenshot of the game window
        '''
        shot = self.d.screenshot(region=(left, top, left+width, top+height))
        rgb = cv.cvtColor(shot, cv.COLOR_BGR2RGB)

        return rgb
