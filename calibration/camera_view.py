import cv2
import pickle

# All this to include camera_utils
from os.path import dirname, abspath
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from camera_utils import Camera

video = cv2.VideoCapture(1)
cam = Camera()
while True:
    ret_val, img = video.read()
    if img is not None:
        img = cv2.flip(img, 1)
        # img = cam.undistort(img)
        small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
        cv2.imshow('my webcam', small)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
        cv2.destroyAllWindows()
