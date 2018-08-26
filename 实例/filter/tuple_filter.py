#coding:utf-8

#为元组中每一个元素命令提高可读性
#方案一定义常量如NAME=0 , AGE=1

#方案二使用namedtuple
from collections import namedtuple
Student1 = namedtuple('Student',['name','age','sex','email'])

s1 = Student1('name1','age1','sex1','email1')
s2 = Student1('name2','age2','sex2','email2')
print s1
print s2
print s1.name
print s2.name



























