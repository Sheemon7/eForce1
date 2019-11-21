import matplotlib.pyplot as plt
import numpy as np
import cv2 
from cut import find_lines_and_center

img = np.load("test_image15.npy")

plt.figure("1")
plt.imshow(img)

o, s, l, r, img = find_lines_and_center(img, 130, 190)

plt.figure("2")
plt.imshow(img, cmap="gray")
plt.scatter([l, s, r], [20 , 20 ,20], c="red", lw=5)
plt.scatter(160, 10, c="blue", lw=5)
print(o, s, l, r)
plt.show()
