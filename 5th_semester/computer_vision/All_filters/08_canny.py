import cv2

img = cv2.imread("./images/charli_noisy.jpeg",0)

edges = cv2.Canny(img, 100 ,200)

cv2.imshow("orignal",img)
cv2.imshow("canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()