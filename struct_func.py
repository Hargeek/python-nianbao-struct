# Name:         struct_func.py
# Description:  
# Author:       honganrong
# Date:         2019-12-12

import struct


def my_send(sk, msg):
    msg_bs = msg.encode("utf-8")
    msg_struct_len = struct.pack("i", len(msg_bs))

    sk.send(msg_struct_len)
    sk.send(msg_bs)


def my_recv(sk):
    # 接收一个数据包
    msg_struct_len = sk.recv(4)
    msg_len = struct.unpack("i", msg_struct_len)[0]
    data = sk.recv(msg_len)
    return data.decode("utf-8")
