# Name:         struct模块说明.py
# Description:
# Author:       honganrong
# Date:         2019-12-12

import struct

# msg = "abcdefg"
# bs = msg.encode('utf-8')
# # print(type(bs))
# # print(bs)
# bs_struct_len = struct.pack("i", len(bs))
# print(bs_struct_len)

# b'\x07\x00\x00\x00'

# 打包，把一个数字打包成字节
# i int 2^32=42亿多长个bit=4GB内容

# bs_struct_len = struct.pack("i", 123456789)
# print(bs_struct_len)   # b'\x15\xcd[\x07'
# print(len(bs_struct_len))  # 4  不论数字大小, 定死了4个字节
#
# # 接收方
# # 把字节还原成数字
bs = b'\x07\x00\x00\x00'

tuple = struct.unpack("i", bs)
print(tuple)  # 输出 (7,)
num = struct.unpack("i", bs)[0]  # 返回的是元祖(123456789,), 取第0个元素
print(num)  # 123456789
print(type(num)) # 输出 int