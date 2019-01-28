# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

def testReadFile():
    '''
        readlines(): 读取所有内容，返回list
        readline(): 读取一行内容
        read(): 读取所有内容
        read(size): 读取size字节内容
     '''

    f = open('PythonIODemo.txt', 'r')
    print(f.read())
    f.close()

def testWriteFile():
    with open('PythonIODemo.txt', 'r') as fo:
        os = fo.read()
    with open('PythonIODemo.txt', 'w') as fi:
        fi.write(os + '\n我写了一个字符串进来了')


#StringIO str 内存读写
from io import StringIO
def testStringIO():
    f = StringIO()
    f.write('字符串')
    f.write(', 对就是字符串')
    f.write(', 我写了三次write才写完。')
    print(f.getvalue())

#BytesIO 二进制数据 内存读写
from io import  BytesIO
def testBytesIO():
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())

if __name__ == '__main__':
    #testReadFile()
    #testWriteFile()
    testStringIO()
    testBytesIO()
    pass