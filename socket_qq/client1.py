from socket_qq.tcp_client_chat import QQClient


if __name__ == '__main__':
    # 登录QQ, 并和服务器建立连接, 模拟登陆
    qq = QQClient('13523456')
    # 开启聊天
    qq.chat('472759903')
