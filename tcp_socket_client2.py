# Name:         tcp_socket_client2.py
# Description:
# Author:       honganrong
# Date:         2019-12-12

import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
time.sleep(5)

bs = sk.recv(1)  # 先接收到下一个数据包的长度
len = int(bs.decode("utf-8"))
bs1 = sk.recv(len)  # 接受对应长度的字节
bs2 = sk.recv(1024)
print(bs1)
print(bs2)
