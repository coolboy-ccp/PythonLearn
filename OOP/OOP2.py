
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#面向对象高级编程
class Person(object):
    # 只允许实例添加tuple中的属性
    # 只对当前类有用，对子类不起作用
    __slots__ = ('name', '_age', 'sex')

    def __init__(self, name = 'Justin', age = '28', sex = '男'):
        self.name = name
        self._age = age
        self.sex = sex

    def __str__(self):
        return 'Hello! I am %s, %s years old. My sex is %s.' % (self.name, self._age, self.sex)
    #__str__使用print显示
    #__repr__调试模式显示
    __repr__ = __str__

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


    pass

def testPerson():
    p = Person()
    p.age = 10
    print(p.age)
    print(p)

# --*-- 多继承 --*--
class Animal(object):
    def __init__(self):
        self.name = '%s' % self.__class__
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('So, %s is Running...' % self.__class__.__name__)

class FlyableMixIn(object):
    def fly(self):
        print('So, %s is flying...' % self.__class__.__name__)

class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, RunnableMixIn):
    pass

class Parrot(Bird, FlyableMixIn):
    pass

class Ostrich(Bird, FlyableMixIn):
    pass

def testMixIn():
    dog = Dog()
    dog.run()
    parrot = Parrot()
    parrot.fly()


if __name__ == '__main__':
    testPerson()
    testMixIn()
    pass