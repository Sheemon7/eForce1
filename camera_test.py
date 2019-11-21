from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (320, 240)
camera.color_effects = (128, 128)
camera.framerate = 32

camera.start_preview()
sleep(5)
camera.capture("/tmp/picture.jpg")
camera.stop_preview()
