# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

import socket, threading

def request(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.184', 8888))
    print(s.recv(1024).decode('utf-8'))
    for data in map(lambda x: ('%s---%d' % (x, i)).encode('utf-8'), ['mike', 'justin', 'branch']):
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

def multiRequest():
    def loop():
        for i in range(5):
            request(i)
    t = threading.Thread(target=loop)
    t.start()


if __name__ == '__main__':
     multiRequest()
