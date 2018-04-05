import random
import cv2
import time

# All this to include camera_utils
from os.path import dirname, abspath
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from camera import Camera

video = cv2.VideoCapture(1)
cam = Camera()
start = time.time()
count = 1
num_imgs = 3
freq = .5 # Hz
while True:
    ret_val, img = video.read()
    img = cam.undistort(img)
    small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
    cv2.imshow('my webcam', small)
    cv2.waitKey(1)
    if time.time() - start > 1/freq:
        print ('img captur ied ' + str(count))
        cv2.imwrite('./calibration/sample_imgs/' + str(random.randint(0, 99999)) + '.png', img)
        start = time.time()
        count += 1
        if count > num_imgs:
            break;
    cv2.destroyAllWindows()
