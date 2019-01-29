# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#多线程

import time, threading, functools


def decorator(f):
    def wrapper(*args, **kw):
        print('thread %s is running...' % threading.current_thread().name)
        f(*args, **kw)
        print('thread %s is ended' % threading.current_thread().name)
    return wrapper

@decorator
def subThreadTarget():
    for i in range(5):
        print(r"thread %s's step >>> %s" % (threading.current_thread().name, i))
        time.sleep(1)

@decorator
def createThread():
    t = threading.Thread(target=subThreadTarget, name='subThread')
    t.start()
    t.join()

#lock

balance = 0

def change_n(n):
    global balance
    balance += n
    balance -= n

#不加锁
def nolock(n):
    for i in range(1000034):
        change_n(i)

#加锁
lock = threading.Lock()
def hasLock(n):
    for i in range(1000034):
        lock.acquire()
        try:
            change_n(i)
        finally:
            lock.release()


def _2thread(f):
    t1 = threading.Thread(target=f, args=(6,))
    t2 = threading.Thread(target=f, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

#ThreadLocal
local_school = threading.local()

def thread_exection():
    print(r"Access %s in %s" % (local_school.student, threading.current_thread().name))

def create_thread(std, name):
    def threadMethod(std):
        local_school.student = std
        thread_exection()
    return threading.Thread(target=threadMethod,args=(std,), name=name)

def testThreadLocal():
    t1 = create_thread('alice', 'thread-one')
    t2 = create_thread('lisa', 'thread-two')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    #_2thread(nolock)
    #_2thread(hasLock)
    #createThread()
    testThreadLocal()
    pass



