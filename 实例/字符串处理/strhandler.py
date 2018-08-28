#coding:utf-8




s = 'ab;cd|ef|hi,jkl|mn\topq;res,uvw\txyz'

#只处理单个分隔符
res =  s.split(";")
#print map(lambda x: x.split("|"),res)


import re

#使用正则表达式进行分割
print re.split('[,;\t|]+', s)

#re.sub()

#str.join()




























