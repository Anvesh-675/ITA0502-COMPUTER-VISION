import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Maruthi\Downloads\MICKEY.png")

kernel = np.ones((5,5), np.uint8)

erode = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
