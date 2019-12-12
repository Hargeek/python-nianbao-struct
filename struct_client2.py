# Name:         struct_client2.py
# Description:  
# Author:       honganrong
# Date:         2019-12-12


import socket
import struct_func as msu
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8123))

time.sleep(5)

print(msu.my_recv(sk))
print(msu.my_recv(sk))