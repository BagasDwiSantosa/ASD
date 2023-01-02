import timeit
# Impor kelas Timer yang ditentukan dalam modul
from timeit import Timer

# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)

#     t = timeit.Timer("random.randrange(%d) in x"%i,
#     "from __main__ import random,l")
#     d_time = t.timeit(number=1000)
#     print(d_time)
# t2 = Timer("test2()", "from __main__ import test2")
# print("append :",t2.timeit(number=1000), "milliseconds")

def test2():
    l = []
    for i in range (1000):
        l.append(i)

def test3():
    l = [1]
    for i in range (1000):
        l.insert(i,i)

t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("insert ",t3.timeit(number=1000), "milliseconds")