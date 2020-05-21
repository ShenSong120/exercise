# _*_ coding: utf-8 _*_
import socket


# 创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定需要监听的端口
server.bind(('localhost', 9090))
# 开始监听(表示可以使用5个链队排队)
server.listen(5)
# conn就是客户端链接过来而在服务端生成的一个链接实例
while True:
    # 等待链接, 多个链接的时候就会出现问题, 起始返回了两个值
    conn, addr = server.accept()
    print(conn, addr)
    while True:
        # 接收数据
        data = conn.recv(1024)
        # 打印接受到的数据
        print('recive: ', data.decode())
        # 然后再发送
        conn.send(data.upper())
    conn.close()
