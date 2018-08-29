#coding:utf-8

#该章节跟音频有关，目前前44个字节保持了音频的相关信息
f = open('bk001.wav','rb')
info = f.read(44)
print info

import struct
print struct.unpack('h',info[22:24])
print struct.unpack('i',info[24:28])#int

import array
f.seek(0,2)
n = (f.tell() - 44) / 2
buff = array.array('h', (0 for _ in xrange(n))) #根据音频数据长度生成数组
f.seek(44)
buff = f.read()
print buff[0]
print buff[55]

#其余部分暂不添加









