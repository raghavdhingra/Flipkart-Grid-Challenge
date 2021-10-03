import numpy as np
import cv2
import cv2.aruco as aruco
 
# aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)  # Use 5x5 dictionary to find markers
matrix_coefficients=np.array([[1.03300138e+04, 0.00000000e+00, 1.46029738e+03],
 [0.00000000e+00, 1.10048373e+04, 2.06794510e+03],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],)
distortion_coefficients=np.array([[ 1.24903917e+00, -6.56401776e+01, -4.92095919e-02, -5.78694877e-02,
   1.05145599e+03]])



def track(matrix_coefficients, distortion_coefficients):
    cap = cv2.VideoCapture(0)  # Get the camera source
    while True:
        ret, frame = cap.read()
        #print(ret)
        # operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Change grayscale
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)  # Use 5x5 dictionary to find markers
        parameters = aruco.DetectorParameters_create()  # Marker detection parameters
# lists of ids and the corners beloning to each id
        corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict,
                                                                parameters=parameters,
                                                                cameraMatrix=matrix_coefficients,
                                                                distCoeff=distortion_coefficients)
      

        if np.all(ids is not None):  # If there are markers found by detector
            for i in range(0, len(ids)):  # Iterate in markers
                # Estimate pose of each marker and return the values rvec and tvec---different from camera coefficients
                rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,
                                                                        distortion_coefficients)
                (rvec - tvec).any()  # get rid of that nasty numpy value array error
                aruco.drawDetectedMarkers(frame, corners)  # Draw A square around the markers
                aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)  # Draw Axis
        # Display the resulting frame
        cv2.imshow('frame', frame)
            # Wait 3 milisecoonds for an interaction. Check the key and do the corresponding job.
        key = cv2.waitKey(3) & 0xFF
        if key == ord('q'):  # Quit
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


track(matrix_coefficients, distortion_coefficients)
