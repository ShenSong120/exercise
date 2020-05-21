# _*_ coding: utf-8 _*_
import socket


# 声明socket类型, 同时生成链接对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立一个链接, 连接到本地的9090端口
client.connect(('localhost', 9090))
while True:
    msg = '欢迎访问菜鸟教程!'
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('recv', data.decode())
client.close()
