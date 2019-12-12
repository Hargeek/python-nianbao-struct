# Name:         tcp_socket_server2.py
# Description:
# Author:       honganrong
# Date:         2019-12-11

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen()

conn, address = sk.accept()

conn.send(b'2')   # 预先告诉对方下一个数据包的长度
conn.send(b'ab')
conn.send(b'cd')