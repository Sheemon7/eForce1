#Import modules
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
#import matplotlib.pyplot as plt
from cut import find_lines_and_center

#Initialize camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.color_effects = (128, 128)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

#Let camera warm up
time.sleep(0.2)
tmp = 0
#start = time.time()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	img = frame.array
	#end = time.time()
	cv2.imshow("Preview", img)
	
	rawCapture.truncate(0)
	od, st, ll, rl, _ =  find_lines_and_center(img, 120, 165)
	print(f"odchylka: {od}, stred: {st}, levy pruh: {ll}, pravy_pruh: {rl}")
	key = cv2.waitKey(1)
	if key == ord("q"):
		print("Quitting")
		break
	if tmp<10:
		np.save(f"test_image{10+tmp}.npy",img)
	#	print(end-start)
		tmp+=1
	
cv2.destroyAllWindows()
camera.close()
