# import cv2
# import numpy as np

# img = cv2.imread("../images/charli_noisy.jpeg",0)

# blur = cv2.GaussianBlur(img, (5,5), 0)

# lap = cv2.Laplacian(blur,cv2.CV_64F)

# zero = np.zeros_like(img)

# rows,cols = lap.shape

# threshold = 10

# for i in range(1,rows-1):
#     for j in range(1, cols-1):

#         patch = lap[i-1:i+2, j-1:j+2]

#         if patch.min() < -threshold and patch.max() > threshold:
#             zero[i,j] = 255

# # slope = first derivative 
# gx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# gy = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# magnitude = cv2.magnitude(gx,gy)

# cv2.imshow("orignal",img)
# cv2.imshow("Gaussian",blur)
# cv2.imshow("Laplacian",cv2.convertScaleAbs(lap))
# cv2.imshow("Zero crossing", zero)
# cv2.imshow("slope",cv2.convertScaleAbs(magnitude))

# cv2.waitKey(0)
# cv2.destroyAllWindows()



