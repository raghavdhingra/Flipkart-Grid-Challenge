import cv2
import matplotlib.pyplot as plt
import numpy as np
 

frame=cv2.imread("./sample.png")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = np.array([60, 35, 140])
upper_blue = np.array([180, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(frame, frame, mask = mask)
plt.imshow(frame)
plt.show()
plt.imshow(mask)
plt.show()
plt.imshow(result)
plt.show()
