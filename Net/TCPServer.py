# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

import socket, threading, time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.0.184', 8888))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        sk, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sk,addr))
        t.start()

def tcplink(sk, addr):
    print('Accept new connection from %s:%s...' % addr)
    sk.send(b'Welcome')
    while True:
        data = sk.recv(1024)
        print('---------------',data)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sk.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sk.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    connect()