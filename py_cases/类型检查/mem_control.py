#coding:utf-8

class A(object):
    def __del__(self):#析构函数
        print 'in A.__del__'

a = A()
import sys
print sys.getrefcount(a)-1

a2 =  a
print sys.getrefcount(a)-1

#a = 5


#在环状数据结构中管理内存
#python垃圾回收器回收对象时，会出现父节点引用子节点，子节点同时也引用父节点的情况，此时同时del引用父子节点，2个对象不能被立即回收
#使用标准库weakref，它可以创建一种访问对象但不增加引用计数的对象

import weakref
a_wref = weakref.ref(a) #生成弱引用
print sys.getrefcount(a)-1
a3 = a_wref()
print sys.getrefcount(a)-1
print a3 is a













