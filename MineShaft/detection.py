import pyautogui
import subprocess
import numpy as np
import cv2 as cv
import math
import mss
import pygetwindow as gw
import os


class detection:

    detect_itemlist = {}

    tofind_img = []
    battle_img = None
    method = None

    def __init__(self):
        '''
        initialize the detection objects
        More objects can be added for detections by providing
        the relative path of image if needed 
        '''
        folder_path = os.path.dirname(os.path.abspath(__file__))

        os.chdir(folder_path)

        
        self.add_detect_item("../cvlearning/player2.png", 0.85, 'player')
        self.add_detect_item("../cvlearning/enemy_bloodbar.png", 0.8, 'enemy')
        self.add_detect_item(
            "../cvlearning/teammate_bloodbar.png", 0.8, 'teammate')

    def detect_item(self, battle_img):
        '''
        this function accepts the screen capture as
        parameter for matchtemplate
        '''
        self.battle_img = battle_img
        '''
        use mss to get the game window location
        '''
        with mss.mss() as sct:
            gameWindow = gw.getWindowsWithTitle('Thetan Arena')[0]

            y = gameWindow.top
            x = gameWindow.left
            win_cor = (x, y)
        
        '''
        conduct matchtemplate for every object
        '''
        for i in range(len(self.tofind_img)):
            result = cv.matchTemplate(
                self.battle_img, self.tofind_img[i][0], cv.TM_CCOEFF_NORMED)

            threshold = self.tofind_img[i][1]

            # set x,y of the player image
            img_w = self.tofind_img[i][0].shape[1]
            img_h = self.tofind_img[i][0].shape[0]

            points = []

            loc = np.where(result >= threshold)

            for (x, y) in zip(*loc[::-1]):

                center_x = int(x) + int(img_w / 2)
                center_y = int(y) + int(img_h / 2)
                points.append((center_x + win_cor[0], center_y + win_cor[1]))

            #   e.g.    detection_point = {"player":point ,"enemy": array of points, 
            #               "teammate" : array of points }

            self.detect_itemlist[self.tofind_img[i][2]] = points

            points = None

        return self.detect_itemlist

    def add_detect_item(self, tofind_img, thershold, item_name):
        '''
        this is the function for initializing the
        image for object detection
        '''
        tofind = cv.imread(tofind_img, cv.IMREAD_UNCHANGED)

        tofind = cv.cvtColor(tofind, cv.COLOR_BGR2RGB)

        
        info = (tofind, thershold, item_name)

        self.tofind_img.append(info)

