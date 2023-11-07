import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg',0)

plt.imshow(img, cmap='gray')
plt.show()
