# purpose: to record video during launch and store locally
from picamera import PiCamera
from time import sleep
import datetime

# file name contains date and time that program is run
filename="vid_{date:%Y-%m-%d_%H:%M:%S}.h264".format(date=datetime.datetime.now())

# Camera Settings
camera = PiCamera()
camera.resolution = (480, 270)    # can be adjusted if save file is too large
camera.framerate = 12               # can be adjusted if save file is too large

# recording
camera.start_preview()
camera.start_recording(filename)    #save file name
sleep(8)         
camera.stop_recording()
camera.stop_preview()