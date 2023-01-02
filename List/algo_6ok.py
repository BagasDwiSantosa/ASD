from gettext import npgettext
from multiprocessing.sharedctypes import Value
import time
def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1,n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start

print("Sum is %d required %10.7f seconds" % sum_of_n(100000))

# Program 2
def sum_of_n2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        value = i
        the_sum = the_sum + value
    end = time.time()
    return the_sum, end - start

print("Sum is %d required %10.7f seconds" % sum_of_n(100000))
print("Sum is %d required %10.7f seconds" % sum_of_n2(100000))

# program 3
def ulang(n):
    ke = 0;
    for i in range(1, n+1):
        for j in range(1, n+1):
            ke = ke + 1
            print(ke)

ulang(5)


# O(n) #digunakan untuk mengelompokkan/mengklasifikasikannya algoritma pemrograman berdasarkan kerumitannya
#emirat8.github.io/article/notasi-big-o/


# buat program untuk menghasilkan bilangan acak sebanyak n, kemudian tampilkan bilangannya secara urut. Hitung waktu yang dibutuhkan.

# from random import randint
# def acak(n):
    
#     for i in range(1, n+1):
#         bil = randint(1,100)
#         print(bil)

# acak(5)

from random import randint
def proses(n):
    bil = [ ]
    for i in range(1,n+1):
        bil.append(randint(1,100))
    
    for i in range(0, n):
        print (bil[i], end=" ")
    print(" ")

    #proses pengurutan
    for i in range(0,n):
        for j in range(0,n):
            if(bil[i]<bil[j]):
                tmp = bil[i]
                bil[i] = bil[j]
                bil[j] = tmp
    
    # menampilkan setelah urut
    for i in range(0,n):
        print(bil[i], end=" ")
proses(5)

