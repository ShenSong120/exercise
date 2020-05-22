# 客户端
import socket
import time
import cv2
import threading
import struct
import numpy

 
class CameraConnectObject:
    def __init__(self, address_port=('localhost', 8880)):
        self.resolution = [640, 480]
        # 客户端对象
        self.client = None
        # 地址以及端口
        self.address_port = address_port
        # 图片播放时间间隔
        self.interval = 0
        # 每秒传输多少帧数
        self.img_fps = 15
        # 双方确定传输视频帧率, (888)为校验值
        self.src = 888 + self.img_fps
        # 提前定义(避免警告)
        self.name = None
        self.buf = None
        self.image = None

    def set_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def socket_connect(self):
        self.set_socket()
        self.client.connect(self.address_port)
        print("IP is %s:%d" % (self.address_port[0], self.address_port[1]))

    def rt_image(self):
        # 按照格式打包发送帧数和分辨率
        self.name = self.address_port[0] + " Camera"
        self.client.send(struct.pack("lhh", self.src, self.resolution[0], self.resolution[1]))
        while True:
            info = struct.unpack("lhh", self.client.recv(8))
            # 获取读的图片总长度
            buf_size = info[0]
            if buf_size:
                try:
                    # 代表bytes类型
                    self.buf = b""
                    temp_buf = self.buf
                    # 读取每一张图片的长度
                    while buf_size:
                        temp_buf = self.client.recv(buf_size)
                        buf_size -= len(temp_buf)
                        # 获取图片
                        self.buf += temp_buf
                        # 按uint8转换为图像矩阵
                        data = numpy.fromstring(self.buf, dtype='uint8')
                        # 图像解码
                        self.image = cv2.imdecode(data, 1)
                        # 展示图片
                    cv2.imshow(self.name, self.image)
                except:
                    pass
                finally:
                    # 每10ms刷新一次图片，按'ESC'(27)退出
                    if cv2.waitKey(5) == 27:
                        self.client.close()
                        cv2.destroyAllWindows()
                        break

    def get_data(self, interval):
        show_thread = threading.Thread(target=self.rt_image)
        show_thread.start()

    # 开始录制视频
    def start_record_video(self):
        self.client.send('shensong'.encode())
        while True:
            print(self.client.recv(1024).decode())
            break


if __name__ == '__main__':
    camera = CameraConnectObject()
    camera.socket_connect()
    camera.get_data(camera.interval)
    time.sleep(5)
    camera.start_record_video()
