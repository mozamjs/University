# checking packges

# import cv2 
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt

# print("OpenCV:", cv2.__version__)
# print("NumPy:", np.__version__)
# print("Matplotlib:", matplotlib.__version__)

# image processing  USING opencv
# import cv2

# img = cv2.imread("test.jpg",0)

# if img is None:
#     print("Image not found")
# else:
#     cv2.imshow("My image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


#using matplotlib

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("test.jpg",1)

# #BGR -> RGB conversion (important)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.title("image using matplotlib")
# plt.axis("off")
# plt.show()


# class code 
# import cv2
# import numpy

# img = cv2.imread("test.jpg",1)

# A = [3, 5, 5, 7, 19, 20]
# print(A[1:4])

# crop = img[0:50, 0:100]
# print(crop)
# print(crop.shape)

# cv2.imshow("IMAGE",crop)
# cv2.waitKey(0)

# print("ok")

# for i in range(1,6):
#     print(i)

# for i in range(1, 4):
#     print(i)

# for i in range (1,4,2):
#     print(i)

# for i in range (3):
    # for j in range (1,4):
        # print(j)


for i in range(1,7):
    for j in range (1,i):
        print(j)