#coding=utf-8

from timeit import Timer

# li1 = [1, 2, 3]
# li2 = [32, 232, 232]
# lis = li1 + li2

# li3 = list(range(10000))

# li4 = [i for i in range(200)]

# li5 = []
# for i in range(1000):
#     li5.append(i)

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

timer1 = Timer('test1()', 'from __main__ import test1')
print('append: ',timer1.timeit(1000)) # 测算次数, 返回值测算时间

timer2 = Timer('test2()', 'from __main__ import test2')
print('+: ',timer1.timeit(1000))

timer3 = Timer('test3()', 'from __main__ import test3')
print('[]: ',timer1.timeit(1000))

timer4 = Timer('test4()', 'from __main__ import test4')
print('list: ',timer1.timeit(1000))
