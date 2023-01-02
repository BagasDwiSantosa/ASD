def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

a = list(range(1000))
def test5():
    a[0] = 100


a = list(range(1000))
def test6():
    b = a.pop()

# Impor modul timeit
import timeit
# Impor kelas Timer yang ditentukan dalam modul
from timeit import Timer
# Jika baris di atas dikecualikan, Anda perlu mengganti Timer dengan timeit.Timer saat mendefinisikan objek Timer
t1 = Timer("test1()", "from __main__ import test1")
print("concat :",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append :",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension :",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range :",t4.timeit(number=1000), "milliseconds")

t5 = Timer("test5()", "from __main__ import test5")
print("index :",t5.timeit(number=1000), "milliseconds")

t6 = Timer("test6()", "from __main__ import test6")
print("pop :",t6.timeit(number=1000), "milliseconds")



# Contoh untuk operasi pop(0) dan pop():
# Buat program berikut
# pop_zero = Timer("x.pop(0)",
# "from __main__ import x")
# pop_end = Timer("x.pop()",
# "from __main__ import x")
# x = list(range(2000000))
# print("pop(0) :",pop_zero.timeit(number=1000))
# x = list(range(2000000))
# print("pop() :",pop_end.timeit(number=1000))



# pop_zero = Timer("x.pop(0)", "from __main__ import x")
# pop_end = Timer("x.pop()", "from __main__ import x")
# print("\ti\t\t\tpop(0)\t\t\tpop()")
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = pop_end.timeit(number=1000)
#     x = list(range(i))
#     pz = pop_zero.timeit(number=1000)
#     print("%15.5f,\t%15.5f,\t%15.5f" %(i,pz,pt))

# insert_a = Timer('x.insert("from__main__import x")')
# append_a = Timer('x.append("from__main__import x")')
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = insert_a.timeit(number=1000)
#     x = list(range(i))
#     pz = append_a.timeit(number=1000)
#     print("%15.5f,\t%15.5f,\t%15.5f" %(i,pz,pt))

# Membandingkan list dan dictionary
# Buat program berikut:
# import timeit
# import random
# print("Perulangan\t\tJumlah Waktu\t\t\tWaktu")
# for i in range(10000,1000001,20000):
#     t = timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d \t\t\t%10.3f\t\t%10.3f" % (i, lst_time, d_time))



# #
