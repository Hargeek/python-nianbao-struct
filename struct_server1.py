# Name:         struct_server1.py
# Description:  
# Author:       honganrong
# Date:         2019-12-12

import socket
import struct


sk = socket.socket()
sk.bind(("127.0.0.1", 8999))

sk.listen()
conn, address = sk.accept()

# 发送数据
msg = input(">>>:")
bs = msg.encode("utf-8")
# 先发长度
msg_len_bs = struct.pack("i", len(bs))
conn.send(msg_len_bs)
# 发数据
conn.send(bs)


# 发送数据
msg = input(">>>:")
bs = msg.encode("utf-8")
# 先发长度
msg_len_bs = struct.pack("i", len(bs))
conn.send(msg_len_bs)
# 发数据
conn.send(bs)
