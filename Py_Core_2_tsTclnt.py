from socket import *
HOST = '127.0.0.1'
# or 'local host'
PORT = 21568
BUFSIZ =1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        # 如果无内容，则close
        break
    print(data.decode('utf-8'))

tcpCliSock.close()

