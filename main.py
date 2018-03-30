import cv2
import numpy as np
import buoy_cv as bcv
from camera_utils import Camera
import os

# Grabs and shuffles the images
data_path = "./data/"
img_dir = os.listdir(data_path)
np.random.shuffle(img_dir)

# img = cv2.imread(data_path + "backg1.jpg")
# center, width = bcv.get_buoy_size(img, True, "backg")

# cam = Camera()

for img_path in img_dir:

    img = cv2.imread(data_path + img_path)
    # img = cam.undistort(img)
    center, width = bcv.get_buoy_size(img, True, img_path)
    # bcv.thresh_detect(img)
