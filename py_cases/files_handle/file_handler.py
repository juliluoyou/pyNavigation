#coding=utf-8

import time
# s = u'你好'
# print s.encode('utf8')
#
# f = open('py2.txt','w+')
# f.write(s.encode('gbk'))
# #f.write(s)#'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# f.close()
#
# time.sleep(1)
#
# f = open('py2.txt', 'r')
# t = f.read()
# print t
# print t.decode('gbk')


#设置文件的缓冲（全缓冲、行缓冲、无缓冲）

#f = open('cache.txt','w+', buffering=2048) #全缓冲，缓冲区大小 > 1

#f = open('cache.txt','w+', buffering=1) #行缓冲，设置缓冲区大小 = 1

#f = open('cache.txt','w+', buffering=0) #无缓冲，设置缓冲区大小 = 0


#将文件映射到内存，使用mmap模块的mmap()函数
import mmap
#od -x demo.bin


#访问文件的状态
#1、文件类型（普通文件、目录、符号链接、设备文件。。。）
#2、文件的访问权限
#3、文件的最后的访问/修改/节点状态更改时间
#4、普通文件大小
#。。。

#系统调用：标准库中os模块下的3个系统调用stat  fstat   lstat获取文件状态
#快捷函数：标准库中os.path下的函数，使用简洁


















