#coding:utf-8

#在构造器中过滤掉非正数的元素
class IntTuple(tuple):
    def __init__(self, iterable):
        #无论是before还是after都无法修改self和iterable的值满足到过滤掉数据的行为
        #before
        super(IntTuple,self).__init__(iterable)
        #after

t = IntTuple([1,-1,'abc',['x','y'],3])
print t

#解决方案：定义类Inttuple继承内置tuple，并实现__new__，修改实例化行为
class IntTuple2(tuple):

    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple2, cls).__new__(cls,g)


    def __init__(self, iterable):
        #无论是before还是after都无法修改self和iterable的值满足到过滤掉数据的行为
        #before
        super(IntTuple2,self).__init__(iterable)
        #after

t = IntTuple2([1,-1,'abc',['x','y'],3])
print t

###################################################################################















