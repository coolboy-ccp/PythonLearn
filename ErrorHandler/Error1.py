# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#错误处理
import logging

#try
def testTry(division = 1):
    try:
        print('trying...')
        r = 10 / int(division)
        print(r)
    except ValueError as e:
        logging.exception(e)
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END...\n')

#raise error
def testRaise():
    n = 0
    if n == 0:
        raise ValueError('test raise a error')
    return 10 / n

#raise to up
def testRaiseToUp():
    try:
        testRaise()
    except ValueError as e:
       # raise #将错误抛到上层调用,错误信息不变
        raise ValueError(r"test raise to up '%s'" % e) #自定义错误信息，屏蔽原错误

if __name__ == '__main__':
    #testTry()
    #testTry(0)
   # testTry('a')
    try:
        testRaiseToUp()
    except ValueError as e:
        print(e)
