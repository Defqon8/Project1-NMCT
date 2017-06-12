from picamera import PiCamera
import time
import  

camera = PiCamera()

print("Making snapshots")
if(led_pin == LOW):
    camera.capture('/home/pi/Snapshot.jpg')
    time.sleep(2)
    camera.capture('/home/pi/Snapshot.jpg')
else:
    camera.stop_preview()