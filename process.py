import cv2
import numpy as np
import matplotlib.pyplot as plt

theimage = cv2.imread('Untitled.jpg')
invert = (255 - theimage)
final = invert / 255.0

plt.imshow(final)
plt.show()
print(final.shape)
(661, 667, 3)

