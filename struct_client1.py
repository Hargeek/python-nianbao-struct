# Name:         struct_client1.py
# Description:  
# Author:       honganrong
# Date:         2019-12-12

import socket
import struct
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 8999))

time.sleep(5)

# 先收长度
bs_msg_len = sk.recv(4)
# 转换成数字
bs_len = struct.unpack("i", bs_msg_len)[0]
bs = sk.recv(bs_len)
print(bs.decode("utf-8"))


# 先收长度
bs_msg_len = sk.recv(4)
# 转换成数字
bs_len = struct.unpack("i", bs_msg_len)[0]
bs = sk.recv(bs_len)
print(bs.decode("utf-8"))