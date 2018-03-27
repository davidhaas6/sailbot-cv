import random
import cv2
import time


cam = cv2.VideoCapture(1)
start = time.time()
while True:
    ret_val, img = cam.read()
    cv2.imshow('my webcam', img)
    cv2.waitKey(1)
    if time.time() - start > 2:
        print 'img captured'
        cv2.imwrite('./img' + str(random.randint(0, 99999)) + '.png', img)
        start = time.time()
    cv2.destroyAllWindows()
