# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2018/07/05 12:52:08

# desc: xjc
import struct
import binascii
import chardet

list_dec = [1, 2, 3, 4, 53, 100, 220, 244, 255]
with open('hexBin.bin', 'wb')as fp:
    for x in list_dec:
        a = struct.pack('B', x)
        fp.write(a)

print('read...........')
with open('hexBin.bin', 'rb')as fp:
    szLine = fp.readline()
    print(len(szLine))
    print(szLine)
    print(binascii.hexlify(szLine))
    print(binascii.unhexlify(binascii.hexlify(szLine)))
    print(struct.unpack("BBBBBBBBB", szLine))

print('done')
