from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for connection...')
    data, addr = udpSerSock.recvfrom(BUFIZ)
    udpSerSock.sendto((b'[%s] %s' % (bytes(ctime(), 'utf-8'), data)), addr)
    print('...received from and returned to:' , addr)

udpSerSock.close()