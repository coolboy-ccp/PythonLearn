
# 高级特性


#切片
def testSlice():
    nums = [1,2,3,4,5,6,7]
    print(nums[:3])
    print(nums[1:3])
    print(nums[-2:])
    #前六个数，每两个截取一个
    print(nums[:6:2])

#迭代
def testIteration():
    dict = {'a':1, 'b':2, 'c':3}
    keys = ''
    values = ''
    kvs = ''
    for key in dict:
        keys = keys + key + ','
    for value in dict.values():
        values = values + '%d' % value + ','
    for k,v in dict.items():
        kvs = kvs + '%s:%d' % (k,v) + ','
    print(keys[:-1], values[:-1], kvs[:-1])

#列表生成式
def testListComprehensions():
    print(list(range(1, 10)))
    print([x * x for x in range(1, 10)])
    print([m + n for m in 'ABC' for n in 'XYZ'])
    lstr = ['Ha', 'HHLK', 'KKF1']
    print([l.lower() for l in lstr])

def mutiTable():
    [print('%s * %s = %s ' %(x, y, x * y), end='\n' if x == y else '\t') for x in range(1, 10) for y in range(1, x + 1)]

def mutiTbale1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(r"%s * %s = %s " % (i, j, i * j), end='\t')
        print(" ")

#生成器
def testGenerator():
    gs = (x * x for x in range(9))
    print(gs)
    gsnums = []
    for s in gs:
        gsnums.append(s)
    print(gsnums)
    fibs = fib(6)
    fibsnums = []
    for f in fibs:
        fibsnums.append(f)
    print(fibsnums)

##斐波那契
#在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

if __name__ == '__main__':
    #mutiTbale1()
    mutiTable()
    #testSlice()
    #testIteration()
    #testListComprehensions()
    #testGenerator()
