import socket
from datetime import datetime
from time import time

host = '192.168.43.137'
port = 5560

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendPic(s, filePath):
    filePathServer=r'C:\Users\waqas\Desktop\BackupData'
    currentTime = datetime.now()
    picName = currentTime.strftime("\%Y.%m.%d-%H%M%S") + '.jpg'
    
    completePath = filePathServer + picName
    print(filePath)
    pic = open(filePath, 'rb')
    chunk = pic.read(1024)
    s.send(str.encode("STORE " + completePath))
    t = time()
    while chunk:
        print("Sending Picture")
        s.send(chunk)
        chunk = pic.read(1024)
    pic.close()
    print("Done sending")
    print("Elapsed time = " + str(time() - t) + 's')
    s.close()
    return "Done sending"




def backup(filePath):
    s = setupSocket()
    response = sendPic(s, filePath)
    return response
