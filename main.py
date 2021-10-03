import cv2
from modules.grid_detection import detect_grid, detect_grid_test
from modules.aruco_detection import detect_aruco, detect_aruco_test

def captureContourCenter(frame):
  contours = detect_grid(frame)
  detect_aruco(frame)
  # print(contours)
  cv2.imshow('frame', frame)

def initCam():
  vid = cv2.VideoCapture(0)
  while True:
    ret, frame = vid.read()
    captureContourCenter(frame)
    
    if cv2.waitKey(300) & 0xFF == ord('q'):
        break
    
  vid.release()
  cv2.destroyAllWindows()

# main function to initiate
# initCam()

# Test Functions
detect_grid_test("./images/arena.png") # image: actual arena
# detect_aruco_test("./images/aruco_marker.png")
