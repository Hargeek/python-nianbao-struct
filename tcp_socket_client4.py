# Name:         tcp_socket_client4.py
# Description:
# Author:       honganrong
# Date:         2019-12-12

import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
time.sleep(5)


def my_recv():
    bs = sk.recv(4)
    chang = int(bs.decode("utf-8"))
    msg = sk.recv(chang)
    print(msg.decode("utf-8"))


my_recv()
my_recv()
my_recv()
