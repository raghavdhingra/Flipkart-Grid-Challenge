import cv2 
import numpy as np
import matplotlib.pyplot as plt


def detect_grid(frame):
    contour_list = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 0, 30)
    contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        (x, y, w, h) = cv2.boundingRect(i)
        contour_list.append([x,y,w,h])
        try:
            if cv2.contourArea(i) > 0:
                cv2.drawContours(frame, i, -1, (0, 0, 255), 3)
                cv2.circle(frame, (x + w//2, y + h//2), 2, (255, 0, 0), 3)
        except:
            continue
    return contour_list


def detect_grid_test(image_src):
    frame = cv2.imread(image_src)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 0, 30)
    contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    xc = 0
    for i in contours:
        (x, y, w, h) = cv2.boundingRect(i)
        try:
            if cv2.contourArea(i)>3000:
                cv2.drawContours(frame, i, -1, (0, 0, 255), 3)
                print(x + w//2, y + h//2)
                cv2.circle(frame, (x + w//2, y + h//2), 2, (255, 0, 0), 3)
        except:
            continue

    plt.imshow(frame)
    plt.show()
    cv2.destroyAllWindows()