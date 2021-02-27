from socket import *
from requests.exceptions import *

HOST = 'server'
PORT = 21587
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.bind(('0.0.0.0',7775))
tcpCliSock.connect(ADDR)

while True:
    try:
         data1 = tcpCliSock.recv(BUFSIZ)
         if not data1:
             break
         print(data1.decode('utf-8'))
    except ConnectionResetError:
        tcpCliSock.close()
    except Exception:
        pass