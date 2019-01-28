# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#调试
#1. print
#2.assert 终端运行时使用-O，可以屏蔽掉assert.==> python3 -O xxx.py
#3.logging(可以指定level:debug, info, warning, error...) ==> logging.basicConfig(level=logging.INFO)
#4.pdb 让程序以单步方式运行 ==》 python3 -m pdb xxx.py ==> 具体用法百度
#5.IDE直接断点调试


#单元测试

class myDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'myDict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

import unittest

class myTest(unittest.TestCase):

    #每个测试方法开始时调用
    def setUp(self):
        print('setup')

    #每个测试方法结束时调用
    def tearDown(self):
        print('tearDown')

    def test_init(self):
        d = myDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_keyerror(self):
        d = myDict()
        with self.assertRaises(KeyError):
            value = d['empty']


if __name__ == '__main__':
    unittest.main()