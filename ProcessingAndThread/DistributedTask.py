# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#分布式进程
import random, time, queue, sys
from multiprocessing.managers import BaseManager

tast_queue = queue.Queue()
result_queue = queue.Queue()


def loop(f):
    for i in range(10):
        f()

class TaskManager(BaseManager):
    def __putTask(self):
        task = self.get_task_queue()
        def creator():
            n = random.randint(0, 10000)
            print('put task %d...' % n)
            task.put(n)
        loop(creator)

    def __getResult(self):
        result = self.get_result_queue()
        def getor():
            r = result.get(timeout=10)
            print('result: %s', r)
        loop(getor)

    def launch(self):
        self.__registerQueue()
        self = TaskManager(address=('', 5000), authkey=b'ccpkey')
        self.start()
        self.__putTask()
        self.__getResult()
        self.shutdown()
        print('master exit')

    def __registerQueue(self):
        TaskManager.register('get_task_queue', callable=lambda: tast_queue)
        TaskManager.register('get_result_queue', callable=lambda: result_queue)
    pass

class TaskWorker:
    def __register(self):
        TaskManager.register('get_task_queue')
        TaskManager.register('get_result_queue')

    def __connect(self):
        self.__register()
        server_addr = '192.168.0.184'
        print('connect to server %s...' % server_addr)
        m = TaskManager(address=(server_addr, 5000), authkey=b'ccpkey')
        m.connect()
        return m

    def work(self):
        m = self.__connect()
        task = m.get_task_queue()
        result = m.get_result_queue()
        def workItem():
            try:
                n = task.get(timeout=1)
                print('run task %d * %d' % (n, n))
                r = '%d * %d = %d' % (n, n, n*n)
                time.sleep(1)
                result.put(r)
            except queue.Empty:
                print('task queue is empty')
        loop(workItem())
        print('worker exit.')
    pass

if __name__ == '__main__':
    #TaskManager().launch()
    #TaskWorker().work()
    pass