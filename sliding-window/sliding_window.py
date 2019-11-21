from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from pyimagesearch.helpers import pyramid
from pyimagesearch.helpers import sliding_window
import argparse
import time
import cv2

model=load_model('model.h5')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and define the window width and height
image = cv2.imread(args["image"])
winW = winH = 32

def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    # only grayscale
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

# loop over the image pyramid
for resized in pyramid(image, scale=1.5):
    # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
            # if the window does not meet our desired window size, ignore it
                if window.shape[0] != winH or window.shape[1] != winW:
                    continue

                # THIS IS WHERE YOU WOULD PROCESS YOUR WINDOW, SUCH AS APPLYING A
                # MACHINE LEARNING CLASSIFIER TO CLASSIFY THE CONTENTS OF THE
                #img = img.reshape(img = np.asarray(img)
                img = cv2.resize(window, (32, 32))
                img = preprocessing(img)
                plt.imshow(img, cmap = plt.get_cmap('gray'))
                img = img.reshape(1, 32, 32, 1)
                probs = model.predict(img)[0]
                c = np.argmax(probs)
                # if probs[c] > 0.5  and c < 2:
                if c < 2:
                    print(c, probs)
                    # since we do not have a classifier, we'll just draw the window
                    clone = resized.copy()
                    cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
                    # cv2.imshow("Window", clone)
                    cv2.imwrite("{}_{}.png".format(c,probs), clone)
                    # cv2.waitKey(1)
                    # time.sleep(10)
