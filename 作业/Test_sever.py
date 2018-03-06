import socket

so = socket.socket()#地址族：family=AF_INET,IPV4 协议类型：type=SOCK_STREAM
"""
创建socket对象
"""
print(so)

address = ('127.0.0.1', 8180)#定义IP地址和端口

so.bind(address)#绑定端口

so.listen(5)#监听端口，决定server端多少客户端可以连上
print('waiting...')

while 1:
    conn, addre = so.accept()#conn 建立客户端与服务器的连接，对应客户端的connect

    while 1:
        try :
            date = conn.recv(1024)
        except Exception:
            break
        if not date:

            break
        print(date.decode('utf-8'))