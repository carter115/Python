# -*- coding: utf-8 -*-

from collections import Iterator,Iterable
import time
import calendar
localtime = time.localtime(time.time())
print(localtime)
print(time.asctime(localtime))

print((x for x in range(10)))
g = (x for x in range(10))
for x in g:
    print(x)

#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print j,'x',i,'=',i*j,'\t',
    print '\n'


print('-'*50)
#斐波那契额
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print b,
#         a,b = b,b+a
#         n += 1
# print(fib(7))


#用generator,如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# print(fib(7))

#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def testYie():
    print("第一次执行到这里")
    yield 1
    print('第二次执行到这里')
    yield 3
    print('第三次执行到这里')
    yield 5
#需要先构造一个函数对象
newTestYie=testYie()

print(next(newTestYie))
print(next(newTestYie))
print(next(newTestYie))


#帕斯卡三角
def triangles(x):
    b = [1]
    while True:
        print(b)
        if x==len(b):
            break
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
triangles(6)


#判断是否是可迭代对象
print(u'第77行判断字符串是否是可迭代对象',isinstance("as",Iterable))
print(u'第78行判断list是否是可迭代对象',isinstance([],Iterable))
print(u'第79行判断字典是否是可迭代对象',isinstance({"aa":123,"cc":123},Iterable))

#转换为Iterator对象
print('第87行Iterable转换为Iterator对象',isinstance(iter([x for x in range(10)]),Iterator))

#continue 语句跳出本次循环，而break跳出整个循环
for x in "HelloWorldhaha":
        if x=="r":
            continue
        print("now word:",x,)
        if x=="a":
            break
#pass 用于保证代码的完整性，不做任何作用

for x in range(10):
    if x%3==0:
        pass
        print("NiHao",)
    print("num",x)


#python的时间对象以一个元组的形式呈现分别为年，月，日，小时，分钟，秒一周第几天，一年第几天，是否夏令时
localtime = time.localtime(time.time())
print(localtime)
#时间格式化
print(time.asctime(localtime))

print(calendar.month(2015,11))
print(calendar.leapdays(2000,2009))