# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#面向对象高级编程

#自定义类型迭代器
class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1

    def __iter__(self):
        return  self

    #迭代支持
    def __next__(self):
        self.__a,self.__b = self.__b, self.__a + self.__b
        if self.__a > 100:
            raise  StopIteration()
        return  self.__a

    #下标支持
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a, b = b, a + b
        return a


def testIter():
    strn = ''
    for n in Fib():
        strn = strn + '%s ' % n
    print(strn)
    print(Fib()[4])

#链式
class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path
    __repr__ = __str__

def testChain():
    chain = Chain().status.user.timeline.list
    print(chain)

#实例直接当成方法调用
class CallableObjc(object):
    def __init__(self, name = 'mike'):
        self._name = name

    def __call__(self, flag): {
        print('my name is %s.%s' % (self._name, flag))
    }

def testCallable():
    co = CallableObjc()
    if callable(co):
        co(1)
        co('flag')

#使用枚举类

from enum import Enum, unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

def testMonth():
    print(Month.Jun.value)
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

def testWeekday():
    if Weekday['Tue'] == Weekday.Tue:
        print(Weekday.Tue.value)
        print(Weekday(1))

if __name__ == '__main__':
    testIter()
    testChain()
    testCallable()
    testMonth()
    testWeekday()