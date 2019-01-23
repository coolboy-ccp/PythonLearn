# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#面向对象编程



class Student(object):
    #类属性，实例和类都可以调用
    school = 'hhxueyuan'

    #name,className是实例属性
    #实例属性的优先级高于类属性，如果二者重名，类属性会被覆盖
    def __init__(self, name, className = "三年二班"):
        self.name = name
        self.className = className
        self.__class = '%s' % self.__class__
        self._a = "aaaa"

    def desc(self,*args):
        print(self._descStr(*args))

    def _descStr(self, *args):
        originStr = self.__class + ': ' + self.name + ' ' + self.className + ' ' + self._limitAge()
        for n in args:
            originStr = originStr + " %s" % n
        return  originStr

    def _limitAge(self):
        return '6岁'

    def __len__(self):
        return self.__sizeof__()
    pass


class SeniorStudent(Student):

    def __init__(self,name, className = '搬砖系1002班'):
        super().__init__(name)
        self.className = className

    def _limitAge(self):
        return '18岁'
    pass

def tStu1():
    stu1 = Student('zhangsan')
    stu1.score = '15分'
    stu1.desc(stu1.score)

def tStu2():
    stu2 = SeniorStudent('dazhangs')
    stu2.score = '400分'
    stu2.desc(stu2.score)
    return stu2

def testType():
    print(type('a'))
    print(isinstance('a', str))
    print(isinstance([1], (tuple, list)))#是否是list，tuple其中一种

def testAttr():
    stu2 = tStu2()
    print(dir(stu2))  # 获取所有属性和方法
    #len方法需要实现__len__()
    print(stu2.__sizeof__(), len(stu2))
    #获取属性
    if hasattr(stu2,'name'):
        setattr(stu2,'name', 'huahua')
        print(getattr(stu2, 'name'))
    print(getattr(stu2, 'sex', 'stu2 has no sex attribute'))

    #获取方法
    if hasattr(stu2, '_limitAge'):
        print(getattr(stu2, '_limitAge')())


if __name__ == '__main__':
    tStu1()
    tStu2()
    testType()
    testAttr()
    pass