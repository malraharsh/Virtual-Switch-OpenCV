import numpy as np
import cv2
import time

import imutils
from imutils.video import FileVideoStream, VideoStream

path = 0
SIZE_WIDTH = 500
SIZE_HEIGHT = 500
COLOR_RED = (0, 0, 255)
TIMER_SETUP = 3
POS_SCREEN = (50, 50)

def get_frame(fvs):
    frame = fvs.read()
    if frame is None:
        return
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=SIZE_WIDTH, height=SIZE_HEIGHT) 
    return frame


def drawbox(bbox, frame, thick=2): #draws rectangle from bbox
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255,0,0), thick, 1)

