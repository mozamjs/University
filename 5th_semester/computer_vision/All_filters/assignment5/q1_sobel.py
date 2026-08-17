import cv2
import numpy as np

img = cv2.imread("../images/charli_noisy.jpeg",0)

blur = cv2.GaussianBlur(img,(3,3),0)

gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

magnitude = np.sqrt(gx**2 + gy**2)

threshold = 100 

_,binary = cv2.threshold(magnitude, threshold,255,cv2.THRESH_BINARY)

gx_display= cv2.convertScaleAbs(gx)
gy_display= cv2.convertScaleAbs(gy)
mag_display= cv2.convertScaleAbs(magnitude)


cv2.imshow("Orignal", img)
cv2.imshow("smooth",blur)
cv2.imshow("Gradient x",gx_display )
cv2.imshow("Gradient Y",gy_display)
cv2.imshow("Gradient Magnitude",mag_display)
cv2.imshow("Threshold",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()












