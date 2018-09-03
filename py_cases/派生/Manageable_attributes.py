#coding:utf-8

#创建可管理的对象属性
#使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError("wrong type.")
        self.radius  = float(value)

    R = property(fget=getRadius, fset=setRadius)

c1 = Circle(1)
c1.radius = 6
print c1.R
c1.R = 5
print c1.R

#重载自定义类的实例之间可以使用<,>,<=,>=等等符号进行比较
#比较符号运算符重载需要实现以下方法：
#__lt__, __le__, __gt__, __ge__, __eq__, __ne__
#使用标准库下的functools下的类装饰器total_ordering可以简化此过程










