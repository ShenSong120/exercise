# _*_ coding: utf-8 _*_


def read_chat(socket):
    """
    读取别人发送过来的数据
    :param socket:
    :return:
    """
    while True:
        try:
            msg = socket.recv(1024).decode()
            # 将接受到的信息 打印到控制台
            print(msg)
        except ConnectionResetError:
            print('服务器连接失败, 请重新链接~')
            break


def write_chat(socket, to_qq):
    """
    发送消息给to_qq
    :param socket:
    :param to_qq:
    :return:
    """
    while True:
        msg = input('请输入要发送给[%s]的消息: ' % to_qq)
        # 准备发送给服务器的内容
        msg = f'{to_qq}:{msg}'
        # 将信息发送给服务器
        try:
            socket.send(msg.encode())
        except ConnectionResetError:
            print('服务器连接失败, 请重新链接~')
            break


def server_chat(socket, socket_mapping):
    """
    服务器处理数据, 并实现两个客户端交互
    :param socket:
    :param socket_mapping:
    :return:
    """
    # 接收客户端身份, 并进行存储
    qq = socket.recv(1024).decode()
    # 存储身份(这里也可以实现不允许同一账户多次登录)
    socket_mapping[qq] = socket
    # 给所有socket显示, 该用户上线了
    for k, v in socket_mapping.items():
        v.send(f'[{qq}上线了]'.encode())

    # 开启循环、用来不断地进行转发数据
    while True:
        try:
            # 接收客户端发送的消息
            data = socket.recv(1024).decode()
            to_qq, msg = data.split(':', 1)
            # 将信息转发给to_qq对应的客户端
            to_socket = socket_mapping[to_qq]
            # 将信息发送给to_socket
            to_socket.send(f'{qq}:{msg}'.encode())
        except ConnectionResetError:
            # 该客户端离线了
            socket_mapping.pop(qq)
            for k, v in socket_mapping.items():
                v.send(f'[{qq}]下线了'.encode())
            # 退出循环
            break
        except KeyError:
            # 该用户不在线、提示fqq, 您的好友不在线
            socket.send(f'您的好友[{to_qq}]不在线'.encode())
