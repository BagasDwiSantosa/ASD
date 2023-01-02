def test1():
    l = []
    for i in range(1000):
        l = l+ [i]

def test2():
    l = []
    for i in range (1000):
        l.append(i)

def test3():
    l = [i for i in range (1000)]

def test4():
    l = list(range(1000))

def pop(l,n):
    del l[n]

def pop():
    l = list(range(1000))
    l.pop(3)

def pop1():
    l = list(range(1000))
    l.pop()

import timeit
from timeit import Timer
# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")

# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")

# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000),
# "milliseconds")

# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000),
# "milliseconds")

# from random import randint
# l = []
# # l = list(range(10))
# for i in range(10):
#     n = randint(1,100)
#     l = l + [n]
# print(l)
# pop(l,3)
# print(l)

t5 = Timer("pop()", "from __main__ import pop")
print("comprehension ",t5.timeit(number=1000),
"milliseconds")

t6 = Timer("pop1()", "from __main__ import pop1")
print("list range ",t6.timeit(number=1000),
"milliseconds")

#pop semakin lama semakin naik
#pop(i) konstan
#O(n) semakin banyak datanya semakin banyak waktunya
#iteration menyesuaikan datanya