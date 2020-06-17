# 服务器端
import socket
import threading
import struct
import time
import cv2
import numpy
from socket_video.camera import ExternalCameraVideo


class CameraService:
    def __init__(self, address_part=("", 8880)):
        # 视频流对象
        self.video = None
        # 摄像头分辨率
        self.resolution = (1600, 800)
        # 图片质量
        self.img_quality = 100
        # 视频帧率
        self.img_fps = 15
        # 地址以及端口
        self.address_part = address_part
        # 服务器对象
        self.server = None
        self.set_socket(self.address_part)

    # 设置套接字
    def set_socket(self, address_part):
        # 创建server对象
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口可复用
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 连接
        self.server.bind(address_part)
        self.server.listen(5)

    # 信息校验
    def check_option(self, cli):
        # 按格式解码，确定帧数和分辨率
        info = struct.unpack('lhh', cli.recv(8))
        if info[0] > 888:
            # 获取帧数
            self.img_fps = int(info[0]) - 888
            self.resolution = list(self.resolution)
            # 获取分辨率
            self.resolution[0] = info[1]
            self.resolution[1] = info[2]
            self.resolution = tuple(self.resolution)
            return True
        else:
            return False

    # 发送图片信息
    def rt_image(self, cli, address):
        if self.check_option(cli) is False:
            return
        # 设置传送图像格式, 图片质量(0-100越大质量越高)
        img_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_quality]
        while True:
            # 读取视频每一帧
            image = self.video.camera_image
            # 按格式生成图片
            _, img_encode = cv2.imencode('.jpg', image, img_param)
            # 将图片转换成矩阵
            img_code = numpy.array(img_encode)
            # 图片对应的矩阵, 生成相应的字符串
            img_data = img_code.tostring()
            try:
                # 按照相应的格式进行打包发送图片
                cli.send(struct.pack("lhh",
                                     len(img_data),
                                     self.resolution[0],
                                     self.resolution[1]) + img_data)
                # 避免cpu占用过高加入延时
                time.sleep(0.04)
            except:
                # 释放摄像头资源
                # camera.release()
                self.video.stop_record_thread()
                return

    # 接收客户端消息
    def receive_client_message(self, cli):
        while True:
            signal = cli.recv(1024).decode()
            if signal == 'start_record':
                # 这里调用开始录制视频的函数
                pass
            elif signal == 'stop_record':
                # 这里调用结束录制视频的函数
                # pass
                # 之后返回视频文件名
                cli.send(signal.encode())


if __name__ == '__main__':
    camera_object = CameraService()
    while True:
        client, address = camera_object.server.accept()
        if address:
            break
    # 创建视频流对象
    camera_object.video = ExternalCameraVideo(video_path='D:/Code/robot/video', video_width=1600, video_height=800)
    time.sleep(2)
    threading.Thread(target=camera_object.rt_image, args=(client, address,)).start()
    threading.Thread(target=camera_object.receive_client_message, args=(client,)).start()

    # # 第一个视频
    # camera_object.video.start_record_video(case_type='test', case_name='123')
    # time.sleep(5)
    # # 模拟机械臂产生一个起始信号
    # camera_object.video.robot_start_flag = True
    # time.sleep(5)
    # camera_object.video.stop_record_video()
