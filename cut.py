import matplotlib.pyplot as plt
import numpy as np
import cv2
import time

def find_lines_and_center(img, ind_1=130, ind_2=190):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img[ind_1:ind_2, :]
    suma = np.sum(img, axis=0)
    left_line = max(0, np.argmin(suma[:120]))
    right_line = 120+ min(120,np.argmin(suma[120:]))
    stred = (right_line+left_line)/2
    odchylka = stred-120
    return odchylka, stred, left_line, right_line, img

"""
img = np.load("test_image.npy")
start = time.time()
od, st, ll, rl, img = find_lines_and_center(img, 120, 165)

print("rychlost fce", time.time()-start)

print("odchylka od stredu", od)

plt.figure()
plt.imshow(img, cmap="gray")
plt.scatter([ll, st, rl], [20,20,20], c="red", lw=5)
plt.scatter(160, 15, c="blue", lw=3)
plt.show()
"""
