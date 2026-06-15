# import cv2


# img = cv2.imread("./images/lena_color.jpeg")
# print(img)
# print(img.shape)

# import cv2

# img = cv2.imread("./images/lena_clean.jpeg",0)

# print(img)
# print(img.shape)

# cv2.imshow("image",img)

# crop = img[0:50, 0:100]
# print (crop)
# print(crop.shape)
# cv2.imshow("IMAGE",crop)

# cv2.waitKey(0)






# image display karna using matplotlib

# import cv2
# import matplotlib.pylab as plt

# img = cv2.imread("./images/lena_clean.jpeg")

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)

# plt.show()

# Grayscale bnana 

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("./images/lena_color.jpeg")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

# plt.imshow(img)
# plt.imshow(gray, cmap = "gray")
# plt.show()



# ............gaussian blur .............

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("./images/lena_noisy_1.jpg")

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

# gaussian = cv2.GaussianBlur(img_rgb, (5,5), 0)

  #jtna bara kernal utna zyada blur hoga, 0 is the standard deviation in X and Y direction, it is calculated from the kernel size

# cv2.imshow("gaussian", gaussian)
# cv2.imshow("original", img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.imshow(img_rgb)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1,2,2)
# plt.imshow(gaussian)
# plt.title("Gaussian Blur")
# plt.axis("off")

# plt.show()



# ..................box filter...............

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("./images/charli_noisy.jpeg")

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# box = cv2.blur(img_rgb,(3,3))

# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.imshow(img_rgb)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1,2,2)
# plt.imshow(box)
# plt.title("Box Filter")
# plt.axis("off")

# plt.show()


# ................ both .............

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("./images/charli_noisy.jpeg")
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# box = cv2.blur(img_rgb,(9,9))
# gaussian = cv2.GaussianBlur(img_rgb,(9,9),0)

# plt.figure(figsize=(15,5))

# plt.subplot(1,3,1)
# plt.imshow(img_rgb)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1,3,2)
# plt.imshow(box)
# plt.title("Box Filter")
# plt.axis("off")

# plt.subplot(1,3,3)
# plt.imshow(gaussian)
# plt.title("Gaussian Filter")
# plt.axis("off")

# plt.show()


# ............custom kernal ..............

# import cv2
# # import matplotlib.pyplot as plt
# import numpy as np

# img = cv2.imread("./images/charli_noisy.jpeg")

# kernal = np.array([
#     [1,1,1],
#     [1,1,1],
#     [1,1,1]], dtype=np.float32)/9

# filtered = cv2.filter2D(img, -1, kernal)


# cv2.imshow("original", img)
# cv2.imshow("Blur", filtered)    

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(kernal)

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread("images/charli_noisy.jpeg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# kernel = np.array([
#     [1,1,1],
#     [1,1,1],
#     [1,1,1]
# ], dtype=np.float32) / 9

# output = cv2.filter2D(img, -1, kernel)

# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1,2,2)
# plt.imshow(output)
# plt.title("Custom Box Filter")
# plt.axis("off")

# plt.show()


# ...............Edge detection...............

import cv2
import numpy as np

img = cv2.imread("./images/charli_noisy.jpeg", cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1]
], dtype=np.float32)

edges = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()