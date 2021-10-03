initial_matrix = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# sorts the contour list into matrix in form of arena for applying aStar algorithm for shortest path
def sort_contour_list_to_matrix(contour_list):
  matrix = []
  l = len(contour_list)
  for i in range(0, l):
      for j in range(0, l-i-1):
          if (contour_list[j][1] > contour_list[j + 1][1]):
              tempo = contour_list[j]
              contour_list[j]= contour_list[j + 1]
              contour_list[j + 1]= tempo

  k = 0
  for i in initial_matrix:
    for j in initial_matrix[i]:
      if initial_matrix[i][j] == 0:
        initial_matrix[i][j] = contour_list[k]
        k = k + 1
  return matrix


def get_robot_drop_point(robot_id):
  if robot_id == 65:
    return [8, 0]
  elif robot_id == 66:
    return [9, 0]
  elif robot_id == 67:
    return [9 ,17]
  elif robot_id == 68:
    return [8, 17]

def get_turn_point(robot_id):
  if robot_id == 65:
    return [8, 7]
  elif robot_id == 66:
    return [9, 8]
  elif robot_id == 67:
    return [9, 9]
  elif robot_id == 68:
    return [8 ,10]


# Determines the initial and the end positions of the robot as per the arena
robot_path_position_matrix = [
                              {
                                "robot": 1,
                                "id": 66,
                                "coord": [
                                  [0, 7],
                                  [8, 0]
                                ],
                                "endpoint": "http://192.168.1.5",
                                "isDropped": False
                              },
                              {
                                "robot": 2,
                                "id": 87,
                                "coord": [
                                  [0, 8],
                                  [9, 0]
                                ],
                                "endpoint": "http://192.168.1.7",
                                "isDropped": False
                              },
                              {
                                "robot": 3,
                                "id": 70,
                                "coord": [
                                  [0, 9],
                                  [9, 17]
                                ],
                                "endpoint": "http://192.168.1.11",
                                "isDropped": False
                              },
                              {
                                "robot": 4,
                                "id": 24,
                                "coord": [
                                  [0, 10],
                                  [8, 17]
                                ],
                                "endpoint": "http://192.168.1.6",
                                "isDropped": False
                              }
                            ]