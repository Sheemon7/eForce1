import matplotlib.pyplot as plt
import numpy as np
import cv2

def cut(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	print(img.shape)
	return img[120:165,:]

img = np.load("test_image.npy")

img = cut(img)
rez = np.sum(img,axis=0)
levy_rez = rez[:160]
pravy_rez = rez[160:]

levy_peak = np.argmin(levy_rez)
pravy_peak = int(img.shape[1]/2)+ np.argmin(pravy_rez)

print(levy_peak, pravy_peak)

print("odchylka od stredu", 160-(pravy_peak+levy_peak)/2)

plt.figure()
plt.imshow(img, cmap="gray")
plt.scatter([levy_peak, (pravy_peak+levy_peak)/2,pravy_peak], [20,20, 20], c="red", lw=5)
plt.scatter(160, 15, c="blue", lw=3)
plt.show()

