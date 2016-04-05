# -*- coding: utf-8 -*-

import os

#递归章程
def Recursive(n):
    if n == 1:
        return 1
    return n*Recursive(n-1)
print(Recursive(5))

#尾递归方式
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def fact(n):
    return fact_iter(n, 1)
print(fact(5))

#打印出1,3,5,7...99
xInt=1
listA=[]
while xInt<=99:
    listA.append(xInt)
    xInt=xInt+2
print(len(listA),listA)

#取出list中前X个项
nList=[]
flagK=4
for i in range(flagK):
    nList.append(listA[i])
print(nList)
#切片操作
print(listA[0:3])
print(listA[-1])
print(listA[-4:-1])
print(list(range(10)))
print(listA[:10:2])
print(listA[::2])
print(listA[::])

print('-'*50)
#使用在元组上
mTuple=(1,2,3,4,5,6,7,8,9,10)
print(mTuple[2:10])
print(mTuple[::])

##字符串的切片
print('helloworld'[2:6])


print('-'*50)
'''
迭代
'''
#python中众多数据类型都可以迭代遍历，甚至是字符串
for value in "abcdefghi":
    print(value)

#迭代一个dic
d={"a":1,"b":2,"1b":3}

for value1 in d:
    print(value1)

for value2 in d.items():
    print(value2)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance(False, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)


print('-'*50)
#多项迭代
for x, y,z in [(1, 1, 3), (3,2, 4), (4,3, 9)]:
    print(x, y,z)
print()
#列表生成表达式
print([x for x in range(20) if x%3==0])
print([m + n for m in 'ABCD' for n in 'XYZ'])
print([di for di in os.listdir('.')])

for k1,k2 in d.items():
    print(k1,"   ",k2)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

mlist = ['Android', 'NIHAO', 'HAha', 'Apple']
print([s.lower() for s in mlist])

L = ['NIHAO', 'HAha', 118, 'Android', None]
print([sa.lower() for sa in L if isinstance(sa, str)==True])


print('-'*50)
#打印金字塔
def printPyramid(level):
    for i in range(level):
        print(' '*(level-i-1) + '*'*(2*i+1))
printPyramid(10)

print('-'*50)
#斐波那契数列前n项和（sn = a1 + a2+...+ an) 递归
def aa(f):
    if f==0:
        return f
    elif f==1:
        return f
    else:
        return aa(f-1)+aa(f-2)
print(aa(6))

def fib():
    a = b = 1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
for num in fib():
    if num > 68:break
    print num,