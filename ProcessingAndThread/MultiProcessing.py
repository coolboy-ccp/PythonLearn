# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#多进程

import os

#-- fork() -- for mac
def testPid():
    print(r"current process '%s' start..." % os.getpid())
    #fork()会把当前进程(父进程)复制一份(子进程),在父进程(子进程id)和子进程(0)各返回一次
    pid = os.fork()
    if pid == 0:
        print(r"Child process %s's parent is %s" % (os.getpid(), os.getppid()))
    else:
        print(r"Process %s created a child %s" % (os.getpid(), pid))

#-- Process -- for all
from multiprocessing import Process

#子线程中执行
def child_run(name):
    print('Child run process %s(%s)' % (name, os.getpid()))

def testProcess():
    p = Process(target=child_run, args=('PythonLearn_MultiProcess',))
    print('start')
    p.start()
    #进程同步
    p.join()
    print('end')

#-- Pool --创建大量子线程
from multiprocessing import Pool
import time, random

def long_time_task(name):
    print(r"Run task %s(%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def testPool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    p.join()
    print('All subprocesses done.')

#-- subprocess --启动子线程

import subprocess

def testSubprocessOutput():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('exit code:',r)

def testSubprocessInput():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

#-- 进程间通信 --Queue, Pipes
#Queue
from multiprocessing import Queue

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a', 'b', 'c', 'd']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)

def testQueue():
    q = Queue()
    qw = Process(target=write, args=(q,))
    qr = Process(target=read, args=(q,))
    qw.start()
    qr.start()
    qw.join()
    qr.terminate()


if __name__ == '__main__':
    #testPid()
    #testProcess()
    #testPool()
    #testSubprocessOutput()
    #testSubprocessInput()
    testQueue()