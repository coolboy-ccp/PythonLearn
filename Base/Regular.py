# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：

'00\d'可以匹配'007'，但无法匹配'00A'；

'\d\d\d'可以匹配'010'；

'\w\w\d'可以匹配'py3'；

.可以匹配任意字符，所以：

'py.'可以匹配'pyc'、'pyo'、'py!'等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

来看一个复杂的例子：\d{3}\s+\d{3,8}。

我们来从左到右解读一下：

\d{3}表示匹配3个数字，例如'010'；

\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；

\d{3,8}表示3-8个数字，例如'1234567'。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。

但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
'''
import re

def testMatch():
    s = r'^\d{3}\-\d{3,8}$'
    print(re.match(s, '010-23456'))

def testSplit():
    s = r'[\s+\;\,]+'
    print(re.split(s,'a b , , ; c  d'))

def testGroup():
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

#正则默认是贪婪匹配
def testGreedy():
    #尽可能多(贪婪)
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    #尽可能少(非贪婪)
    print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#预编译一个需要大量使用的正则
def testCompile():
    re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
    print(re_tel.match('010-1235678').groups())

if __name__ == '__main__':
    #testMatch()
    #testSplit()
    #testGroup()
    #testGreedy()
    testCompile()