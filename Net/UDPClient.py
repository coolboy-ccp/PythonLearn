# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

import socket

def UDPClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'lisa', b'hanmeimei']:
        s.sendto(data, ('192.168.0.184', 8888))
        print(s.recv(1024).decode('utf-8'))
    s.close()

if __name__ == '__main__':
    UDPClient()