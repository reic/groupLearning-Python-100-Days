from socket import socket
from datetime import datetime
from socket import socket, SOCK_STREAM, AF_INET
import urllib
from time import time
from threading import Thread
import requests

# 繼承 Thread 類別，自定義線程


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # self.url.rfind("/")+1 是找出檔案名稱的位置
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open("./"+filename, 'wb') as f:
            f.write(resp.content)


def main1():
    geturl = ["http://1.bp.blogspot.com/-8ub1VUFP9Ko/Tw0swOBYtEI/AAAAAAAAK0Y/dCzNoHbfNt8/s1600/thunderbird1.jpg",
              "http://3.bp.blogspot.com/-ZPQOFR_vQNI/Tw0s7gKkMVI/AAAAAAAAK0g/UuqMYj-nssc/s320/thunderbird2.jpg"]
    for url in geturl:
        DownloadHandler(url).start()
    #  中文檔名處理的方法
    a = "https://1.bp.blogspot.com/-NJ4Ro-KQoWc/XmskmbvQZRI/AAAAAAAAnDw/dOXklA7vi24M1zT00nTuGHp3BYwKGVxwgCLcBGAsYHQ/s320/%25E6%258A%2593%25E5%258F%2596%25E6%25A8%25A3%25E8%25B2%258C.png"
    a = a[a.rfind('/')+1:a.rfind('.')]
    a = a.replace("%25", " ").lstrip()
    print(bytes.fromhex(a).decode('utf-8'))

    # print(strangeFN.decode('utf-8'))


def telnet_server():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.31.69', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


def client():
    client = socket()
    client.connect(('192.168.31.69', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == "__main__":
    # main()
    pass
