import numpy as np 
import cv2

img = cv2.imread('./images/lena_noisy.jpeg',0)

# there is no any builtin function for prewitt filter in opencv so we have to mannualy create the kernal for prewitt filter

kernel_x = np.array([
    [-1,0,1],
    [-1,0,1],
    [-1,0,1]
    ],dtype = np.float32)

kernel_y = np.array([
    [-1,-1,-1],
    [0, 0, 0],
    [1, 1, 1]
    ],dtype = np.float32)

dx = cv2.filter2D(img,cv2.CV_64F, kernel_x)
dy= cv2.filter2D(img, cv2.CV_64F, kernel_y)

# magnitude = np.sqrt(dx**2 + dy**2)
magnitude = cv2.magnitude(dx, dy)

cv2.imshow("orignal", img)
cv2.imshow("dX", cv2.convertScaleAbs(dx))
cv2.imshow("dY", cv2.convertScaleAbs(dy))

cv2.imshow("Magnitude",
           cv2.convertScaleAbs(magnitude))

cv2.waitKey(0)
cv2.destroyAllWindows()