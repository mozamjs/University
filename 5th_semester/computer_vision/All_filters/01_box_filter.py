import cv2
import numpy as np

print(cv2.__version__)


img = cv2.imread('./images/lena_noisy.jpeg',0)

# kernal =  np.ones((3,3), dtype = np.float32)/9

# filtered = cv2.filter2D(img, -1, kernal)

box_filter= cv2.blur(img, (5,5))


cv2.imshow("orignal", img)
cv2.imshow("Box Filtered", box_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()