import cv2
from modules.grid_detection import detect_grid, detect_grid_test
from modules.aruco_detection import detect_aruco, detect_aruco_test
from modules.utils import sort_contour_list_to_matrix, get_turn_point, get_robot_drop_point, robot_path_position_matrix
from modules.pathDetection import get_smallest_path_aStar,test_smallest_path
import requests
import time

def detect_aruco_and_send_command(frame, robot, smallest_path):
  robot_id = robot["id"]
  endpoint = robot["endpoint"]
  turn_point = get_turn_point(robot_id)
  for i in [66, 87, 70, 24]:
    robot_position = detect_aruco(frame, i, smallest_path)
    if robot_position == turn_point and robot_id in [66, 87]:
      requests.get(endpoint + "/rotate/right/90")
    elif robot_position == turn_point and robot_id in [70, 24]:
      requests.get(endpoint + "/rotate/left/90")
    elif robot_position == get_robot_drop_point(robot_id):
      requests.get(endpoint + "/stop")
      if not robot["isDropped"]:
        requests.get(endpoint + "/drop")
        time.sleep(1)
        requests.get(endpoint + "/retract")
        robot["isDropped"] = True
      else:
        if robot["id"] == 87:
          initCam(1)
        elif robot["id"] == 70:
          initCam(2)
        elif robot["id"] == 24:
          initCam(3)
    else:
      requests.get(endpoint + "/move/forward")


def captureContourCenter(frame,robot):
  contour_list = detect_grid(frame)
  sorted_matrix = sort_contour_list_to_matrix(contour_list)
  smallest_path_list = get_smallest_path_aStar(sorted_matrix,robot["coord"][0],robot["coord"][1])
  detect_aruco_and_send_command(frame,robot,smallest_path_list)
  # print(contours)
  cv2.imshow('frame', frame)

def initCam(robot_index):
  vid = cv2.VideoCapture(0)
  while True:
    ret, frame = vid.read()
    captureContourCenter(frame,robot_path_position_matrix[robot_index])
    
    if cv2.waitKey(300) & 0xFF == ord('q'): # 3.33 fps
        break
    
  vid.release()
  cv2.destroyAllWindows()

# main function to initiate
initCam(0)

# Test Functions
# detect_grid_test("./images/arena.png") # image: actual arena
# detect_aruco_test("./images/aruco_marker.png")
# test_smallest_path()
# detect_aruco_and_send_command()
