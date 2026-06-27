import cv2
import numpy as np

img = cv2.imread('./images/lena_noisy.jpeg',0)

kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
],dtype= np.float32)

# just sharp the image 

sharp = cv2.filter2D(img, -1, kernal)  # -1 ka matlb same data type  age uint8 tha to output bhi uint8 

# first smooth then sharpen the image

filtered = cv2.GaussianBlur(img, (3,3), 0)

sharp2 = cv2.filter2D(filtered, -1, kernal)

cv2.imshow("orignal", img)
cv2.imshow("Sharpened", sharp)
cv2.imshow("Sharpened + Gaussian", sharp2)

cv2.waitKey(0)
cv2.destroyAllWindows()


