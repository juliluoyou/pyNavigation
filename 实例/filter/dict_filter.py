#coding:utf-8
from random import randint

###实例一
##过滤列表中的数据
d = {x:randint(60,100) for x in xrange(1,21)}
print d

print {k:v for k,v in d.iteritems() if v>90}

#集合解析
data = [1,-5,-3,-2,6,8,9]
s = set(data)#list to set
print s

print { x for x in s if x%3 ==0}


###根据字典中的值大小对字典中的项进行排序
#背景：使用内置函数sorted直接进行排序只会对key进行排序
d = {x: randint(60,100) for x in 'xyzabc'}
print sorted(d)

#方法1：使用zip将字典数据转化元组，目的是调转key和value的位置，但是方法不通用
print zip(d.itervalues(),d.iterkeys())
print sorted(zip(d.itervalues(),d.iterkeys()))

#方法2：传递sorted函数的key参数
print sorted(d.items(), key=lambda x : x[1])

###如何让字典保持有序
#背景,无法根据赋值的顺序进行输出
d={}
d['z'] = (1,25)
d['b'] = (2,35)
d['a'] = (3,45)
for k in d: print k

#方法1：使用OrderedDict
from collections import OrderedDict
d=OrderedDict()
d['z'] = (1,25)
d['b'] = (2,35)
d['a'] = (3,45)
for k in d: print k

























