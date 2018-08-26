#coding:utf-8
import timeit

###实例一
##过滤列表中的负数

#常用做法
data = [1,-5,-3,-2,6,8,9]
res=[]
for x in data:
    if x>=0:
        res.append(x)
print res

#filter函数
from random import randint

data = [randint(-10,10) for _ in xrange(10)]
print data

data2 = filter(lambda x:x>=0, data)
print data2

func1 = """
data = [1,-5,-3,-2,6,8,9]
filter(lambda x:x>=0, data)
"""
#print timeit.timeit(func1, number=100000)

#列表解析
print [x for x in data if x>=0]
func1 = """
data = [1,-5,-3,-2,6,8,9]
[x for x in data if x>=0]
"""
#print timeit.timeit(func1, number=100000)

#统计序列中元素出现的频度
data = [randint(-10,10) for _ in xrange(20)]
from collections import Counter
c2 = Counter(data)
print c2[0] #对应位置的出现次数
print c2.most_common(2)

#对文本进行词频统计
import re
txt = open("SQLQuery10.sql").read()
#print txt

c3 =  Counter(re.split('\W+',txt))#简单示例分割
print c3
print c3.most_common(3)


###队列功能
#背景：使用固定长度的队列记录用户的输入的数字
from collections import deque
q = deque([],5) #长度为5的队列
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print q
q.append(6)
print q

import pickle
pickle.dump(q, open("history","w+")) #把q对象写到文件中

import time
print "read the file"
time.sleep(1)
q2 = pickle.load(open("history"))   #从文件中读取内容并赋值给q2对象
print q2

