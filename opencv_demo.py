import cv2
import matplotlib.pyplot as plt

img = cv2.imread('im.png',0)

plt.imshow(img, cmap='gray')
plt.show()
print("Last line of code")
