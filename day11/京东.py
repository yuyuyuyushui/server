import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost', 8090))
server.listen(5)

while True:
    connetion,address = server.accept()
    buf = connetion.recv(1024)
    print(buf.decode())
    with open('test1.html', 'rb') as f:
        date = f.read()
    connetion.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n','utf-8'))
    connetion.sendall(date)
    connetion.close()
