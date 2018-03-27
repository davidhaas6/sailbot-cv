import numpy as np
import cv2
import glob
import os
import pickle

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the chess_imgs.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

img_dir = '../chess_imgs/'
images = glob.glob(img_dir + '*.png') + glob.glob(img_dir + '*.jpg')
print images

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

    # If found, add object points, image points (after refining them)
    if ret:
        objpoints.append(objp)

        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7, 6), corners, ret)
        cv2.imshow('img', img)
        cv2.waitKey(250)

    else:
        print 'removed image'
        os.remove(fname)
        images.pop(fname)

cv2.destroyAllWindows()

et, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

with open('../calibration_vals.pkl', 'wb') as f:
    pickle.dump([et, mtx, dist, rvecs, tvecs],f)

tot_error = 0
for i in xrange(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error
print "mean error: ", tot_error/len(objpoints)
