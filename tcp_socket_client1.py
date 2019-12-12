# Name:         tcp_socket_client1.py
# Description:  
# Author:       honganrong
# Date:         2019-12-11

import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
time.sleep(5)

bs1 = sk.recv(1024)
bs2 = sk.recv(1024)
print(bs1)
print(bs2)
