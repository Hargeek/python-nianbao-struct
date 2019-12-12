# Name:         struct_server2.py
# Description:  
# Author:       honganrong
# Date:         2019-12-12

import socket
import struct_func as msu

sk = socket.socket()

sk.bind(("127.0.0.1", 8123))

sk.listen()
conn, addr = sk.accept()

msu.my_send(conn, "abcdefg")
msu.my_send(conn, "1234567")