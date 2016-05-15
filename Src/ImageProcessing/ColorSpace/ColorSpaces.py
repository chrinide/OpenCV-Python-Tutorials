#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'lh'
__version__ = '1.0'
__date__ = '03/04/2015'


import sys
sys.path.append("../../../")

import cv2
import cv2.cv as cv
import numpy as np

from Src.ToolBox.CameraCapture import CameraCapture


if __name__ == '__main__':
    Cam = CameraCapture(0)
    Resolution = (640, 480)
    Cam.open(resolution=Resolution)
    while True:
        Img = Cam.takePhoto()

        if Img is not None:
            HSV = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)
            H, S, V = cv2.split(HSV)
            LowerBlue = np.array([100, 50, 50])
            UpperBlue = np.array([140, 255, 255])
            mask = cv2.inRange(HSV, LowerBlue, UpperBlue)
            BlueThings = cv2.bitwise_and(Img, Img, mask=mask)
            cv2.imshow('Mask', mask)
            cv2.imshow('Img', Img)
            cv2.imshow('H', H)
            cv2.imshow('Blue', BlueThings)
            # cv2.imshow('S', S)
            # cv2.imshow('V', V)
            Key = chr(cv2.waitKey(15) & 255)
            if Key == 'q':
                break
    Cam.release()
    cv2.destroyAllWindows()
