
import picamera
from datetime import datetime
from cookieClient_FINAL import backup



picPath = "/home/pi/Desktop/piturecomm/images/"

def captureImage(currentTime, picPath):
    
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

while True:
    currentTime = getTime()
    picName = captureImage(currentTime, picPath)
    print("Took a picture")
    completePath = picPath + picName
    backup(completePath)
    print("Backup complete.")
    break  