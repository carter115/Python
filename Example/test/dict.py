# -*- coding: utf-8 -*-

'''dict,set,function'''


'''
字典dict
键-值（key-value）存储，具有极快的查找速度。为什么反复提起查询速度，
因为如果你一个用list只是为了获取里面X元素内容的话性能是相对比较查的，
极力推荐“字典”，字典也在第三片文章中有列出，但是这里还是再丰富下他的一些常用方法。
'''
dic = {'wjj':185,'wmm':175}
print(dic['wjj'])
print('wjj' in dic)
print(dic.get('wjaaj',3))   # 使用get的方法，并且可以指定返回值
print(dic.get('wjaaj'))

dic.setdefault('wgg',102)  # 添加某个键值对
print(dic)

dic.pop('wmm')  # 移除某个键值对
print(dic)

'''
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而增加；
需要占用大量的内存，内存浪费多。
'''

'''
集合set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，
所以，在set中，没有重复的key，类似于list和dict的结合体。
'''
print('-'*30)
sets = set([1,1,1,3,6,3])   # set会自动去重
print(sets)

sets.add('12')  # 向set里添加元素
print(sets)

sets.remove(1)  # 删除某一个元素
print(sets)


'''
函数
'''
print(max(1,21,2,5))
print(abs(-10),abs(100))
# 遍历是否都为真
print(all([True,True,True]),all([True,False,True]),all([3>2,True,True]))
# 遍历部分是否为真
print(any([True,True,True]),any([True,False,True]),any([3>2,True,True]))

print('-'*30)
'''
数据类型转换是我们碰到常有的事，
例如：用户input一个价格为’123’字符串进来，我们需要把他转成整型或者浮点型才可以进行操作。
'''
print(isinstance(12,str))   # False
print(int('123'))
print(str(100)+'Hello',float('10.34'),int(17.3241),bool(1))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，
# 相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

def strToint(s):
    intValue = int(s)
    return intValue
print(strToint('123'))


'''
匿名函数
'''
addAll=lambda arg1,arg2,arg3:arg1+arg2+arg3
print(addAll(2,3,4))

