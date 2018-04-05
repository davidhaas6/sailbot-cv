import cv2
import pickle
import os
import numpy as np

class Camera:
	def __init__(self, disable_video=False, video_channel=1, calibration_path="./calibration/calibration_vals.pkl"):
		# Load the undistortion parameters
		with open(calibration_path, 'rb') as f:
			DIMS, camera_matrix, dist = pickle.load(f)
			self.map1, self.map2 = cv2.fisheye.initUndistortRectifyMap(camera_matrix, dist, np.eye(3), camera_matrix, DIMS, cv2.CV_16SC2)

		self.DIMENSIONS = DIMS # width and height
		self.FOCAL_LEN_X = camera_matrix[0][0] # The X focal length

		fov_rad = 2 * np.arctan((self.DIMENSIONS[0]/(2 * self.FOCAL_LEN_X)))
		self.FOV = np.degrees(fov_rad)

		if not disable_video:
			self.video_capture = cv2.VideoCapture(video_channel)

	def get_frame(self, mirrored=False, undistorted=False):
		if self.video_capture.isOpened():
			retval, frame = self.video_capture.read()
			if retval:
				if mirrored:
					frame = cv2.flip(frame, 1)
				if undistorted:
					frame = self.undistort(frame)
				return frame
		return False

	def undistort(self, img):
		return cv2.remap(img, self.map1, self.map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
