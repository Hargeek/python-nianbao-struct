# Name:         tcp_socket_server4.py
# Description:
# Author:       honganrong
# Date:         2019-12-11

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen()
conn, address = sk.accept()


def my_send(msg):
    # header
    bs = msg.encode('utf-8')
    # 先发数据包的长度，表示长度的数据包占4个字节(4byte)
    chang = len(bs)
    chang_str = format(chang, "04d")  # 长度的数据包格式化成4个字节
    conn.send(chang_str.encode("utf-8"))  # 把长度发送出去
    # content
    # 发数据
    conn.send(bs)


my_send(input(">>>"))
my_send(input(">>>"))
my_send(input(">>>"))
