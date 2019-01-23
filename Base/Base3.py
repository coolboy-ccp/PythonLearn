# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

#返回闭包时，不要引用任何循环变量，或者后续会发生变化的数量
##闭包，返回一个函数sum，sum需要在后续代码中调用
def lazy_sum(*args):

    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def testLazySum():
    f = lazy_sum(*range(1, 5))
    print(f())


#如果非要使用循环变量
def count():
    def f(x):
        def g():
            return x * x

        return g
    return  map(lambda x: f(x), range(1, 4))

def testCount():
    f = map(lambda x: x(), count())
    print(list(f))

#装饰器
def log(text):
    def decorator(f):
        #防止装饰后的函数名变成wrapper
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, f.__name__))
            return f(*args, **kw)
        return wrapper
    return decorator


@log("调用了")
def testDecorator():
    print("我是测试: %s", testDecorator.__name__)


#偏函数
def testInt2():
    int2 = functools.partial(int, base = 2)
    print(int2('10101010'))

def testMax2():
    max2 = functools.partial(max, 10, 20)
    print(max2(2,3,4))


if __name__ == '__main__':
    testLazySum()
    testCount()
    testDecorator()
    testInt2()
    testMax2()