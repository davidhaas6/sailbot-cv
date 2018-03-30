import cv2
import pickle
import os
import numpy as np

class Camera:
    def __init__(self):
        # Load the undistortion parameters
        with open('./calibration/calibration_vals.pkl', 'rb') as f:
            DIMS, camera_matrix, dist = pickle.load(f)
            self.map1, self.map2 = cv2.fisheye.initUndistortRectifyMap(camera_matrix, dist, np.eye(3), camera_matrix, DIMS, cv2.CV_16SC2)

    def undistort(self, img):
        return cv2.remap(img, self.map1, self.map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
