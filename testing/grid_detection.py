import cv2 
import numpy as np 
import matplotlib.pyplot as plt
  
image = cv2.imread("sample1.png")  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 0, 30)
_, contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of Contours found = " + str(len(contours))) 

cv2.imshow("edges",cv2.resize(edged,(500,500)))
cv2.waitKey(0)
xc=0
for i in contours:
            (x, y, w, h) = cv2.boundingRect(i)
            try:
                if cv2.contourArea(i)<8000 and mask:
                    # print("rectangle")
                    cv2.putText(image, 'Building', (x,y), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 1, cv2.LINE_AA)
                    cv2.drawContours(image, i, -1, (0, 255, 0), 3) 
                    print([x,y,w,h])
                    print(x + w//2, y + h//2)
                    cv2.circle(image, (x + w//2, y + h//2), 2, (0, 255, 0), 3)
            except:
                continue
plt.figure()
plt.imshow(image)
plt.show()
print("total rectangle",xc)
cv2.imshow('Contours', cv2.resize(image,(500,500))) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

