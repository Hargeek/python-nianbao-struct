# Name:         tcp_socket_client3.py
# Description:
# Author:       honganrong
# Date:         2019-12-12

import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
time.sleep(5)

# bs = sk.recv(1)   # 先接收到下一个数据包的长度
bs = sk.recv(4)  # 固定数据包的长度为4
# bs = sk.recv(1024) # 可以查看一下所有数据包的长度
chang = int(bs.decode("utf-8"))
msg = sk.recv(chang)
print(msg.decode("utf-8"))