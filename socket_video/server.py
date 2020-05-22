# 服务器端
import socket
import threading
import struct
import time
import cv2
import numpy
from socket_video.camera import ExternalCameraVideo


class CameraAcceptObject:
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
def check_option(obj, cli):
    # 按格式解码，确定帧数和分辨率
    info = struct.unpack('lhh', cli.recv(8))
    print(info)
    if info[0] > 888:
        # 获取帧数
        obj.img_fps = int(info[0]) - 888
        obj.resolution = list(obj.resolution)
        # 获取分辨率
        obj.resolution[0] = info[1]
        obj.resolution[1] = info[2]
        obj.resolution = tuple(obj.resolution)
        return True
    else:
        return False


# 发送图片信息
def rt_image(obj, cli, address):
    if check_option(obj, cli) is False:
        return
    # 设置传送图像格式, 图片质量(0-100越大质量越高)
    img_param = [int(cv2.IMWRITE_JPEG_QUALITY), obj.img_quality]
    while True:
        # 读取视频每一帧
        obj.img = obj.video.camera_image
        # 按格式生成图片
        _, img_encode = cv2.imencode('.jpg', obj.img, img_param)
        # 将图片转换成矩阵
        img_code = numpy.array(img_encode)
        # 图片对应的矩阵, 生成相应的字符串
        obj.img_data = img_code.tostring()
        try:
            # 按照相应的格式进行打包发送图片
            cli.send(struct.pack("lhh", len(obj.img_data), obj.resolution[0],
                                 obj.resolution[1]) + obj.img_data)
        except:
            # 释放摄像头资源
            # camera.release()
            obj.video.stop_record_thread()
            return


if __name__ == '__main__':
    camera_object = CameraAcceptObject()
    while True:
        client, address = camera_object.server.accept()
        if address:
            break
    # 创建视频流对象
    camera_object.video = ExternalCameraVideo(video_path='D:/Code/robot/video', video_width=1600, video_height=800)
    time.sleep(5)
    clientThread = threading.Thread(target=rt_image, args=(camera_object, client, address,))
    clientThread.start()

    # # 第一个视频
    # camera_object.video.start_record_video(case_type='test', case_name='123')
    # time.sleep(5)
    # # 模拟机械臂产生一个起始信号
    # camera_object.video.robot_start_flag = True
    # time.sleep(5)
    # camera_object.video.stop_record_video()
