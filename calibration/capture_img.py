import random
import cv2
import time


cam = cv2.VideoCapture(1)
start = time.time()
count = 1
num_imgs = 10
freq = 1 # Hz
while True:
    ret_val, img = cam.read()
    small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
    cv2.imshow('my webcam', small)
    cv2.waitKey(1)
    if time.time() - start > 1/freq:
        print ('img captured ' + str(count))
        cv2.imwrite('./calibration/chessboard_imgs/' + str(random.randint(0, 99999)) + '.png', img)
        start = time.time()
        count += 1
        if count > num_imgs:
            break;
    cv2.destroyAllWindows()
