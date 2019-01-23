
from functools import reduce

def funcPoint(x, y, f):
    return f(x) + f(y)

def testFP():
    f = abs
    print (funcPoint(-1,-2,f))

def f(x):
    return  x * x

def testMap():
    array = [1,2,3,4,5,6,7]
    array = map(f, array)
    print(list(array))

def fn(x, y):
    return x * 10 + y


def testReduce():
    array = [1, 2, 3, 4, 5, 6, 7]
    num = reduce(fn, array)
    print(num)

def charToNum(x):
    return int(x)

def testReduceStr():
    str1 = '1234567'
    num = reduce(fn, map(charToNum, str1))
    print(num)

def testLambda():
    str1 = '98090909090'
    l = lambda x, y: x * 10 + y
    num = reduce(l, map(charToNum, str1))
    print(num)

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def testPrimes():
    nums = []
    for n in primes():
        if n < 100:
            nums.append(n)
        else:
            break
    print(nums)


def testSorted():
    lista = sorted([2,4,3,6,-1,3,-7,-2],key=abs, reverse=True)
    print(lista)
    listb = sorted(['Jha', 'CCC', 'bba', 'LmK'],key=str.lower)
    print(listb)

if __name__ == '__main__':
    testFP()
    testMap()
    testReduce()
    testReduceStr()
    testLambda()
    testPrimes()
    testSorted()


