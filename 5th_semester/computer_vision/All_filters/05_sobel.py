# import cv2
# import numpy as np
# img = cv2.imread("./images/lena_noisy.jpeg",0)

# # dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# # dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)


# cv2.imshow("orignal",img)
# cv2.imshow("sobel X", cv2.convertScaleAbs(dx))
# cv2.imshow("sobel Y", cv2.convertScaleAbs(dy))

# magnitude = cv2.magnitude(dx, dy)

# cv2.imshow("Magnitude",cv2.convertScaleAbs(magnitude))


# cv2.waitKey(0)
# cv2.destroyAllWindows()





import cv2
import numpy as np
img = cv2.imread("./images/lena_noisy.jpeg",0)  

kernal_x = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
],dtype = np.float32)

kernal_y = np.array([
    [-1,-2,-1],
    [0, 0, 0],
    [1, 2, 1]
],dtype = np.float32)


dx = cv2.filter2D(img, cv2.CV_64F, kernal_x)
dy = cv2.filter2D(img, cv2.CV_64F, kernal_y)

cv2.imshow("orignal", img)
cv2.imshow("sobel X", cv2.convertScaleAbs(dx))
cv2.imshow("sobel Y", cv2.convertScaleAbs(dy))
magnitude = np.sqrt(dx**2 + dy**2)
cv2.imshow("Magnitude", cv2.convertScaleAbs(magnitude))

cv2.waitKey(0)
cv2.destroyAllWindows()













































