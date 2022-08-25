import os
import cv2
import pyautogui
import numpy as np


class cv_matching:
    def preload_templates(self):
        """Preload all images on start to optimize runtime

        Images loaded:
        - "../SourcePictures/findmatch2.png"
        - "../SourcePictures/deathmatch2.png"
        - "../SourcePictures/tutor.png"
        - "../SourcePictures/entertutor2.png"
        - "../SourcePictures/finishtutor.png"
        """
        # ensure relative path
        folder_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(folder_path)

        # opencv read images for template matching
        self.findmatch2_png = cv2.imread(
            "../SourcePictures/findmatch2.png",
            cv2.IMREAD_UNCHANGED)
        self.deathmatch2_png = cv2.imread(
            "../SourcePictures/deathmatch2.png",
            cv2.IMREAD_UNCHANGED)
        self.tutor_png = cv2.imread(
            "../SourcePictures/tutor.png",
            cv2.IMREAD_UNCHANGED)
        self.entertutor2_png = cv2.imread(
            "../SourcePictures/entertutor2.png",
            cv2.IMREAD_UNCHANGED)
        self.finishtutor_png = cv2.imread(
            "../SourcePictures/finishtutor.png",
            cv2.IMREAD_UNCHANGED)

        self.sift = cv2.SIFT_create()
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        self.matcher = cv2.FlannBasedMatcher(index_params,search_params)

    def find_location(self, tofind):
        """Fine the location of image on screen

        Instead of using `pyautogui.locateOnScreen()` OpenCV template matching
        is used after `pyautogui.screenshot()`

        Parameters
        ----------
        tofind: numpy.array
            Template image to be matched on sreen
        """
        # screen capture using pyautogui 
        screen = pyautogui.screenshot()

        # change the capture to numpy array
        img = np.array(screen)

        '''
        since the matchtemplate() function requires 2 images with same format
        so the below code is to convert the images to RBG format
        '''
        tofind = cv2.cvtColor(tofind, cv2.COLOR_BGR2RGB)
        background = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        '''
        the below opencv function matchTemplate() receive 3 parameters, first 2 are images in 
        numpy array, the third one is the opencv comparison algorithm. The function returns
        a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel 
        match with template.
        '''
        result = cv2.matchTemplate(background,tofind,cv2.TM_CCOEFF_NORMED)
        '''
        the below minMaxLoc() function receives a parameter which is a grayscale image
        then return 4 parameters:
        1. the  thershold value of minimum match objects
        2. the  thershold value of maximum match objects
        3. the  coordinates of minimu match objects
        4. the  coordinates of maximum match objects
        '''
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        '''
        the methond only returns the thershold value and location of the most suitable matching object
        '''
        return max_loc,max_val

    def match_location(self, query_img, train_img):
        query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
        train_img_bw = cv2.cvtColor(train_img,cv2.COLOR_BGR2GRAY)

        queryKeypoints, queryDescriptors = self.sift.detectAndCompute(query_img_bw, None)
        trainKeypoints, trainDescriptors = self.sift.detectAndCompute(train_img_bw, None)

        matches = self.matcher.knnMatch(queryDescriptors,
                                        trainDescriptors,
                                        k=2)
        matchesMask = [[0,0] for i in range(len(matches))]
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]

        return len(matchesMask) > 10

        # for mat, mask in zip(matches, matchesMask):
        #     if mask[0]:
        #         mat[0].queryIdx
