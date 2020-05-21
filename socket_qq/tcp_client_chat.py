import socket
import threading
from socket_qq import chat


class QQClient:
    """
    QQ client
    """
    def __init__(self, qq):
        """
        初始化qq号, 并建立连接
        :param qq:
        """
        self.qq = qq
        # 创建socket客户端
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        self.client.connect(('localhost', 8888))
        # 发送自己的身份, 给到服务器
        self.client.send(self.qq.encode())

    def chat(self, to_qq):
        """
        和谁聊天
        :param to_qq:
        :return:
        """
        # 开启两个线程, 分别接收(读取)数据, 和发送(写入)数据
        threading.Thread(target=chat.read_chat, args=(self.client,)).start()
        threading.Thread(target=chat.write_chat, args=(self.client, to_qq,)).start()
