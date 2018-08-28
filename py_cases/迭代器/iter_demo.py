#coding:utf-8

###可迭代对象（迭代器对象__iter__()、序列__getitem__()）、迭代器
###从迭代器对象获取迭代器

##迭代器介绍
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def getWeather(city):
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s: %s , %s ' % (city, data['low'], data['high'])

#['北京','长春','广州']
#print getWeather("北京")
#print getWeather("长春")

from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s ' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

#for x in WeatherIterator(['北京','长春','广州']): print x


##使用生成器函数实现迭代对象
##生成器对象
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2 : return False

        for i in xrange(2, k):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k #（正向迭代）

#for x in PrimeNumbers(1, 100): print x


##反向迭代
##reversed(l) 获取反向迭代器
##iter(l) 获取正向迭代器
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

#for x in FloatRange(1.0,4.0,0.5):print x
#for x in reversed(FloatRange(1.0,4.0,0.5)):print x

##切片操作
from itertools import islice
f = open('SQLQuery10.sql')
#for x in islice(f, 1, 5): print x #需要注意他会消耗原来的迭代对象，即下标无法自动初始化


##在一个for循环中迭代多个可迭代对象,并行
from random import randint

chinese = [randint(60,100) for _ in xrange(40)]
math = [randint(60,100) for _ in xrange(40)]
english = [randint(60,100) for _ in xrange(40)]
#print zip(chinese, math, english)#并行

##在一个for循环中迭代多个可迭代对象,串行
from itertools import chain
e1 = [randint(60,100) for _ in xrange(2)]
e2 = [randint(60,100) for _ in xrange(3)]
e3 = [randint(60,100) for _ in xrange(4)]
e4 = [randint(60,100) for _ in xrange(5)]
count =0
for s in chain(e1,e2,e3,e4):
    if s > 90:
        count +=1
print count




























