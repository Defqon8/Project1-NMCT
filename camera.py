from picamera import PiCamera
import time
camera = PiCamera()

print("Making Snapshots")
while True:
    camera.capture('/home/pi/Snapshot.jpg')
    time.sleep(4)
    camera.capture('/home/pi/Snapshot.jpg')
    time.sleep(4)