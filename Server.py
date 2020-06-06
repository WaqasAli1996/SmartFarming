import socket

host= ''
port= 5560



def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print("socket bind complete")
    return s

def setupConnection():
    s.listen(1)
    conn, address=s.accept()
    print("connected to: " + address[0] + ":" + str(address[1]))
    return conn

def storeFile(filePath):
    print(filePath)
    picFile =open(filePath,'wb')
    print("opened the file")
    pic = conn.recv(1024)
    while pic:
        print("picture is being received")
        picFile.write(pic)
        pic = conn.recv(1024)
    picFile.close()
def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        dataMessage = data.split(' ',1)
        command=dataMessage[0]
        if command == 'STORE':
            print("Store command recieved.Picture will be saved soon:")
            storeFile(dataMessage[1])
            reply = 'file stored'
        elif command == 'EXIT':
            print("our client has left us")
        elif command == 'KILL':
            print("our server is studing down")
            s.close()
            break
        else:
            reply = 'Unknown Command'

        conn.sendall(str.encode(reply))
        print("data has been sent")
    #conn.close()
        
s=setupServer()
while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break


conn = setupConnection()
