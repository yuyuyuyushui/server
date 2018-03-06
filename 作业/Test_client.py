import socket
sk  = socket.socket()

print(sk)
address = ('127.0.0.1',8180)

conn = sk.connect(address)#连接本地服务器IP
while not conn:
    string = input('>>')
    if string == 'e':
        break
    sk.send(string.encode('utf-8'))
