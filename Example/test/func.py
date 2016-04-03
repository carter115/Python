# -*- coding: utf-8 -*-

'''
http://blog.csdn.net/z_Dendy/article/details/42460709
'''

'''
1.函数:map,reduce,filter

map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的
每个元素，并把结果作为新的list返回。
'''
def formatStr(ss):
    return ss[0].upper() + ss[1:len(ss)].lower()

s = ['AASDa','dendY']
# print(formatStr('sdddQQ'))
for v in map(formatStr,s):
    print(v)


# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
print('-'*30)
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
L = [2,3,4]
def prod(a,b):
    return a*b
print(reduce(prod,L))

S = ['z','y','x']
def strabc(a,b):
    return a+b
print(reduce(strabc,S))


# filter函数，方法同map，目的是过滤list中符合条件的元素
print('-'*30)
s = [1,2,-3,-5]
def notlt0(x):
    return x >= 0
# print(filter(notlt0,s))
for i in filter(notlt0,s):
    print(i)
# 定义一个notLt0的方法，该方法用于判断元素是否大于等于0，是则返回True，
# 否则返回False。而filter则会将列表s的每一个元素作为参数调用notLt0方法，
# 最后将所有返回True的元素重新组装成一个list返回。


# 匿名函数：无须定义函数的名称，格式如下：
print('-'*30)
# fn = lambda #函数参数列表: 函数体
# 其中fn为返回的匿名函数，例如：
'''
2.匿名函数
'''
f = lambda x : x * x
print(f(3))


# 函数的闭包，类似javascript的闭包，即外部函数返回内部函数的引用，
# 内部函数可能持有外部函数变量的引用，例如：
print('-'*30)
'''
3.闭包
http://www.jb51.net/article/65479.htm
'''
# 闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。这个返回的函数B就叫做闭包。
# 你在调用函数A的时候传递的参数就是自由变量。举个例子：
def func(name):
    def inner_func(age):
        return 'name:', name, 'age:', age
    return inner_func
bb = func('the5fire')
print(bb(26))  # >>> name: the5fire age: 26
# 这里面调用func的时候就产生了一个闭包——inner_func,并且该闭包持有自由变量——name，
# 因此这也意味着，当函数func的生命周期结束之后，name这个变量依然存在，
# 因为它被闭包引用了，所以不会被回收。

print('-'*30)
def make_adder(addend):
  def adder(augend):
    return augend + addend
  return adder
p = make_adder('abc')
q = make_adder('xyz')
print p('mmm')
print q('nnn')
'''
分析一下:
我们发现,make_adder是一个函数,包括一个参数addend,比较特殊的地方是这个
函数里面又定义了一个新函数,这个新函数里面的一个变量正好是外部make_adder的参数.
也就是说,外部传递过来的addend参数已经和adder函数绑定到一起了,形成了一个新函数,
我们可以把addend看做新函数的一个配置信息,配置信息不同,函数的功能就不一样了,
也就是能得到定制之后的函数.
'''

print('-'*30)
def hellocounter (name):
    count=[0]
    def counter():
        count[0] += 1
        print 'Hello,',name,',',str(count[0])+' access!'
    return counter
hello = hellocounter('ma6174')
hello()
hello()
hello()
'''
分析一下
这个程序比较有趣,我们可以把这个程序看做统计一个函数调用次数的函数.
count[0]可以看做一个计数器,没执行一次hello函数,count[0]的值就加1。
也许你会有疑问:为什么不直接写count而用一个列表?这是python2的一个bug,
如果不用列表的话,会报这样一个错误:
UnboundLocalError: local variable 'count' referenced before assignment.
'''

print('-'*30)
def makebold(fn):
  def wrapped():
    return "<b>" + fn() + "</b>"
  return wrapped
def makeitalic(fn):
  def wrapped():
    return "<i>" + fn() + "</i>"
  return wrapped
@makebold
@makeitalic
def hello():
  return "hello world"
print hello()   #执行结果：<b><i>hello world</i></b>
'''
简单分析
怎么样?这个程序熟悉吗?这不是传说的的装饰器吗?对,这就是装饰器,其实,装饰器就是一种闭包,
我们再回想一下装饰器的概念:对函数(参数,返回值等)进行加工处理,生成一个功能增强版的一个函数。
再看看闭包的概念,这个增强版的函数不就是我们配置之后的函数吗?区别在于,
装饰器的参数是一个函数或类,专门对类或函数进行加工处理。
python里面的好多高级功能，比如装饰器，生成器，列表推到，闭包，匿名函数等，
开发中用一下，可能会达到事半功倍的效果！
'''


'''
4.装饰器(decorator)，包装目标函数，在不改变原目标函数的情况下，对其进行包装，实现更多的功能。
'''
print('-'*30)
# 定义一个装饰器(decorator)
def log(fn):
    def wrapper(*args, **kw):
        print('call : %s' % (fn.__name__))
        return fn(*args, **kw)
    return wrapper
@log
def func():
    print ('hello!')
func()
'''
其中，log函数为一个装饰器，除了完成fn函数本身的功能外，还添加了打印日志的功能，
log函数返回一个装饰函数wrapper，打印的结果：
call : func
hello!

Python中使用@符号来表示装饰器（不是java的注解，形式类似），在执行func函数时，解释器看到@符号标识，
会先执行log方法，并将func函数作为参数，此时func函数依然存在，但是同名的func变量会指向wrapper函数：
print(func.__name__)

输出wrapper，同：
func = wrapper(*args, **kw):
         print('call : %s' % (fn.__name__))
         return fn(*args, **kw)
所以，执行func()函数其实执行的是wrapper函数。
'''

print('-'*30)
# 自定义文本的装饰器
def log(text):
    def decorator(fn):
        def wrapper(*args, **kw):
            print('log : %s, function name : %s. ' % (text, fn.__name__))
            fn(*args, **kw)
        return wrapper
    return decorator

@log('this is a log text.')
def func():
    print ('hello!')
func()
print(func.__name__) # 输出：wrapper
'''
如上，我们需要再定义一个函数decorator来接收我们定义的参数信息，除了上边的执行过程外，在调用func函数时，
解释器会先执行log和decorator函数，最后在执行wrapper函数，形式如下：
func = log(自定义参数)(func)
'''

print('-'*30)
'''
5.偏函数，functools.partial，固定函数参数，形成新的函数：
如果我们需要在转换为int的时候确定进制，Python提供了int方法：
int(x, base = 10)
base为此时x的进制数，默认为10，我们写一个将二进制字符串转换为int的方法：
'''
def int2(x):
    return int(x,base=2)
s = int2('110')
print(s)
# 当然，该函数用法有很多，例如将max函数默认与一些元素比较：
import functools
max2 = functools.partial(max, 10, 20, 30)
s = max2(1, 2, 3, 40)
print(s) # 输出：40
s = max2(1, 2, 3)
print(s) # 输出：30
# 这样，max函数在比较的元素中，默认会加入10,20,30了。