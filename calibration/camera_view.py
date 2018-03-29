import cv2
import pickle

with open('./calibration/calibration_vals.pkl', 'rb') as f:
    et, mtx, dist, rvecs, tvecs = pickle.load(f)
    print (mtx, dist)

def undistort_img(img):
    h, w = img.shape[:2]
    print(w,h)
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    # print(mtx, dist, roi)
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x, y, w, h = roi

    if w==0:
        print("ERROR: ROI IS 0 - " + str(roi))
        exit(-1)
    return dst[y:y + h, x:x + w]

cam = cv2.VideoCapture(1)
while True:
    ret_val, img = cam.read()
    if img is not None:
        img = cv2.flip(img, 1)
        # img = undistort_img(img)
        small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
        cv2.imshow('my webcam', small)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
        cv2.destroyAllWindows()
