# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#操作文件和目录
import os

def testOSInfo():
    print('name:', os.name)
    print('uname:', os.uname())
    print('environ: ', os.environ)
    print('environ.PATH: ', os.environ.get('PATH'))

def aTestNewPath():
    abspath = os.path.abspath('.')
    newpath = os.path.join(abspath, 'testNewDir')
    return newpath

def testCreateDir():
    try:
        os.mkdir(aTestNewPath())
    except FileExistsError as e:
        print(e)

def testDelDir():
    try:
        os.rmdir(aTestNewPath())
    except FileNotFoundError as e:
        print(e)

def testDirInfo():
    allDirPaths = [x for x in os.listdir('.') if os.path.isdir(x)]
    print(allDirPaths)

    allPyFiles = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
    print(allPyFiles)




if __name__ == '__main__':
    #testOSInfo()
    #testCreateDir()
    #testDelDir()
    #testDirInfo()
    pass

