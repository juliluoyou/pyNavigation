#coding:utf-8

#对于一些大型游戏，每一个用户就要实例化一个类，此时需要考虑如何降低对象的内存开销
#使用__slots__
class Player(object):
    def __init__(self,uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    __slots__ = ['uid','name','stat','level'] #描述实例有哪些属性
    def __init__(self,uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('1','a')
p2 = Player2('2','b')

print set(dir(p1))-set(dir(p2))
#Result: set(['__dict__', '__weakref__'])
#__dict__是为了实例可以动态判定字典,但牺牲内存为代价

p1.__dict__['y'] = 9
print p1.y

import sys
print sys.getsizeof(p1.__dict__) #272
print sys.getsizeof(p2) #72































