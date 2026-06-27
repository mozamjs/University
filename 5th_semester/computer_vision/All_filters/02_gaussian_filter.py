import numpy as np
import cv2

img  = cv2.imread("./images/lena_noisy.jpeg",0)

# use buitin function 

filtered = cv2.GaussianBlur(img, (3,3), 0)

# try mannual 
# kernal = np.array([
#     [1,2,1],
#     [2,4,2],
#     [1,2,1]
# ],dtype = np.float32)/16

# filtered = cv2.filter2D(img, -1, kernal)



cv2.imshow("orignal", img)
cv2.imshow("Gaussian Filtered", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
