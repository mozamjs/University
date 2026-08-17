# Image -> Guassian Blur -> Laplacian -> zero Crossing -> Ginal Edges
# pahla blur ->  ku ka laplacian noise ka lia boht sensitive hota ha chota sa noise bhi laplacian ko edge lagta ha 

# zero corssing -> sirf ya check karo positive ka bad negative aya ? ya negitive ka bad positive aya?  agr han  to wo -> Edge ha  -8 -3 -1 2 7  ab -1 la bad 2 aya sign change hua yahin edge hai   5,4,3,2,1 sub positive koi edge nhi  -1 -2 -4 -5  sab negative no edge

# (-) -> (+)   ya (+) -> (-)     ya  (+) -> (0) -> (-) ya    (-) -> (0) -> (+)
#  open cv ma direct koi built in function nhi marr-hildreth ka lia  

import cv2
import numpy as np
 
img = cv2.imread("./images/lena_noisy.jpeg",0)

# step 1 
blur = cv2.GaussianBlur(img,(5,5),0)

# step2
lap = cv2.Laplacian(blur, cv2.CV_64F)

#step 3

# zero = np.zeros_like(lap, dtype=np.uint8)

# rows, cols = lap.shape

# for i in range (1, rows-1):
#     for j in range (1, cols-1):

# center = lap[i,j] #eg : center = -5   right = 10   -5*10 = -50  negative aya matlb sign change hua -> Edge

#         right = lap[i, j+1]

#         if center * right < 0:
#             zero[i,j] = 255

# step 3.0

# zero = np.zeros_like(img)

# rows, cols = lap.shape

# for i in range(1, rows-1):
#     for j in range(1, cols-1):

#         patch = lap[i-1:i+2, j-1:j+2]  # patch ma negative bhi ha positive bhi ha  -> TO BIch ma khi na khi zero crossing hui ho gi[[-4,-2, 1],[-3,-1,2],[-2,1,3]]->   MIN = -4  , MAX = 3

#         if patch.min() < 0 and patch.max() > 0:
#             zero[i,j] = 255

# problem: small change also detected because of this image is too white so the solution is apply threshold 

zero = np.zeros_like(img)

rows, cols = lap.shape

# optional print
print ("min", lap.min())
print("max",lap.max())


threshold = 15

for i in range(1, rows-1):
    for j in range(1, cols-1):

        patch = lap[i-1:i+2, j-1:j+2]

        if patch.min() < -threshold and patch.max() > threshold:
            zero[i,j] = 255


cv2.imshow("Orignal", img)
cv2.imshow("Gaussian",blur)
cv2.imshow("Laplacian",cv2.convertScaleAbs(lap))
cv2.imshow("Zero Crossing",zero)

cv2.waitKey(0)
cv2.destroyAllWindows()

