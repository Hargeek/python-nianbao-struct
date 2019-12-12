# Name:         tcp_socket_server3.py
# Description:
# Author:       honganrong
# Date:         2019-12-11

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen()

conn, address = sk.accept()
msg = input("请输入你要发送的数据>>>:")

# header
bs = msg.encode('utf-8')
# 先发(字节)数据包的长度，表示长度的数据包占4个字节(4byte)
chang = len(bs)
# 把长度变成定长的字符串
chang_str = format(chang, "04d")  # 长度的数据包格式化成4个字节
conn.send(chang_str.encode("utf-8"))  # 把长度发送出去

# content
# 发数据
conn.send(bs)