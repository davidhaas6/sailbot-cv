import cv2
import pickle
import os
import numpy as np

with open('./calibration/calibration_vals.pkl', 'rb') as f:
    DIMS, camera_matrix, dist = pickle.load(f)
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(camera_matrix, dist, np.eye(3), camera_matrix, DIMS, cv2.CV_16SC2)

def undistort(img):
    return cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

path = "./calibration/chessboard_imgs_old/";
imgs = os.listdir(path)

for fname in imgs:
    img = cv2.imread(path + fname)
    if img is not None:
        img = undistort(img)
        small = cv2.resize(img, (0,0), fx=0.6, fy=0.6)
        cv2.imshow(fname, small)
        cv2.waitKey(0)
