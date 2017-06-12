from picamera import PiCamera
import time

camera = PiCamera()

print("Making snapshots")
while True:
    camera.capture('/home/pi/Snapshot.jpg')
    time.sleep(2)
    camera.capture('/home/pi/Snapshot.jpg')
