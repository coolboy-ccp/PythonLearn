# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

import socket

def UDPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('192.168.0.184', 8888))
    print('Bind UDP on 8888...')
    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s' % data, addr)
    pass


if __name__ == '__main__':
    UDPServer()