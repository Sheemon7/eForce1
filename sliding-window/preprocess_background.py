import numpy as np
import matplotlib.pyplot as plt
from pyimagesearch.helpers import pyramid
from pyimagesearch.helpers import sliding_window
import argparse
import time
import cv2
import os

X = np.zeros((11568, 32, 32, 3))
# X = np.zeros((1000, 32, 32, 3))

cc = 0
for imfile in os.listdir("background_imgs"):
    # load the image and define the window width and height
    image = cv2.imread("./background_imgs/" + imfile)
    winW = winH = 32

    # loop over the image pyramid
    for resized in pyramid(image, scale=1.5):
        # if cc == 500:
        #     break
        # loop over the sliding window for each layer of the pyramid
            for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
                # if the window does not meet our desired window size, ignore it
                    if window.shape[0] != winH or window.shape[1] != winW:
                        continue

                    print(cc)

                    # exp_window = np.expand_dims(window, axis=0)
                    # X[cc, :, :, :] = exp_window
                    X[cc, :, :, :] = window
                    # print(X.shape)
                    cc += 1
                    # if cc == 1000:
                    #     break

                    # since we do not have a classifier, we'll just draw the window
                    # clone = resized.copy()
                    # cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
                    # cv2.imshow("Window", clone)
                    # cv2.waitKey(1)
                    # time.sleep(0.01)

np.save("background_imgs.npy", X)
