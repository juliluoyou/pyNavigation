#coding=utf-8

import time
s = u'你好'
print s.encode('utf8')

f = open('py2.txt','w+')
f.write(s.encode('gbk'))
#f.write(s)#'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
f.close()

time.sleep(1)

f = open('py2.txt', 'r')
t = f.read()
print t
print t.decode('gbk')






