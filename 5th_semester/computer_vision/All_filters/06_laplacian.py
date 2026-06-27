#  first Derivative -> Intensity change detect karta hai
#  Second Derivative -> Intensity ke change ka change detect karta hai

# built in function for laplacian filter in opencv is cv2.Laplacian() function

# By using Built in function 

# import cv2
# import numpy as np 


# img = cv2.imread("./images/lena_noisy.jpeg",0)

# lap = cv2.Laplacian(img, cv2.CV_64F)

# lap =  cv2.convertScaleAbs(lap)

# cv2.imshow("orignal", img)
# cv2.imshow("Laplacian", lap)

# cv2.waitKey(0)
# cv2.destroyAllWindows()






# Manually creating the kernal for laplacian filter

import cv2
import numpy as np

img = cv2.imread("./images/lena_noisy.jpeg",0)

kernal = np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0]
],dtype=np.float32)

kernal_8neighbour = np.array([
    [1,1,1],
    [1,-8,1],
    [1,1,1]
],dtype=np.float32)

blur = cv2.GaussianBlur(img, (5,5),0)

#  agar gaussian nhi karn ga to noice bhi age bn jati ha laplacian ma 

lap = cv2.filter2D(blur,cv2.CV_64F,kernal)
# lap = cv2.filter2D(blur,cv2.CV_64F,kernal_8neighbour)

lap = cv2.convertScaleAbs(lap)

cv2.imshow("orignal", img)  
cv2.imshow("Laplacian", lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
