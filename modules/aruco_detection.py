import numpy as np
import cv2
import cv2.aruco as aruco
 
matrix_coefficients=np.array([[1.48286299e+03, 0.00000000e+00, 7.43843828e+02],
 [0.00000000e+00, 1.37020864e+03, 1.98815800e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

distortion_coefficients=np.array([[-0.05738903,  0.98552337, -0.038323, 0.01682442, -2.36926914]])

aruco_5 = aruco.DICT_5X5_250


def detect_aruco(frame, ind, smallest_path):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  aruco_dict = aruco.Dictionary_get(aruco_5)
  parameters = aruco.DetectorParameters_create()
  corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters, cameraMatrix=matrix_coefficients, distCoeff=distortion_coefficients)
  if np.all(ids is not None) and ids == ind:
    for i in range(0, len(ids)):
      rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients, distortion_coefficients)
      (rvec - tvec).any()
      aruco.drawDetectedMarkers(frame, corners)
      aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
  # cv2.imshow('frame', frame)
  # key = cv2.waitKey(0) & 0xFF
  # cv2.destroyAllWindows()
  print (smallest_path)

def detect_aruco_test(image_src):
  frame = cv2.imread(image_src)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
  parameters = aruco.DetectorParameters_create()
  corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters, cameraMatrix=matrix_coefficients, distCoeff=distortion_coefficients)

  if np.all(ids is not None):
    for i in range(0, len(ids)):
      rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients, distortion_coefficients)
      (rvec - tvec).any()
      aruco.drawDetectedMarkers(frame, corners)
      aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
  cv2.imshow('frame', frame)
  key = cv2.waitKey(0) & 0xFF
  cv2.destroyAllWindows()