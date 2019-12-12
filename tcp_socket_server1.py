# Name:         tcp_socket_server1.py
# Description:  
# Author:       honganrong
# Date:         2019-12-11

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen()

conn, address = sk.accept()

conn.send(b'ab')
conn.send(b'cd')
