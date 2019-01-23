import math


def move(x, y, step, angel=0):
    tx = x + step * math.cos(angel)
    ty = y + step * math.sin(angel)
    return tx, ty

def testMove():
    point = move(10, 10, 20)
    print('test', point[0], point[1])

def person(name, age, **other):
    print('name: ', name, ', age: ', age, ', other: ', other)

def testPerson():
    info = {'sex': 'Female', 'city': 'dazh'}
    person('jerry', 18, **info)

def student(name, classname = '三年二班', city = 'small'):
    print('name: ', name, ', classname: ', classname, ', city: ', city)

def testStudent():
    student('dashuang')
    student('xiaoshuang','二年三班')
    student('zhongzheng',city='jjili')

def numbersM(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
    print('numbersM:',sum)

def testNumbersM():
    nums = [1,2,3,4]
    numbersM(*nums)
    numbersM(10,20)

def person1(name,*,city,job):
    print('name:', name,', city: ', city, ', job: ',job)

def testPerson1():
    person1('john',city='bj',job='teacher')

def f1(a,b,*nums,**kw):
    print('a = ', a, 'b = ', b, 'nums = ', nums, 'kw = ', kw)

def testF1():
    nums = [1,2,3]
    kw = {'city':'changsha'}
    f1(*nums,**kw)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fact_iter(num, rt):
    if num == 1:
        return  rt
    return fact_iter(num-1, num * rt)

if __name__ == '__main__':
    testMove()
    testPerson()
    testStudent()
    testNumbersM()
    testPerson1()
    testF1()
    print(fact(6))
    print(fact_iter(6,1))



