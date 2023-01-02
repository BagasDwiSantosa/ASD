#BILANGAN GANJIL GENAP

# bilangan = int(input('Masukkan Bilangan\t:'))

# if bilangan % 2 == 0 :
#     print(str(bilangan)+ ' adalah bilangan genap')
# else :
#     print(str(bilangan)+ ' adalah bilangan ganjil')



# def is_even(n, step):
#     step = step+1
#     return(n%2==0, step)

# step = 0
# number = int(input("Masukkan Bilangan\t:"))
# even, step = is_even(number, step)
# if(even):
#     print("Bilangan {} adalah Genap".format(number))
# else:
#     print("Bilangan {} adalah Ganjil".format(number))

# print("Number of step\t: {}".format(step))


#BILANGAN RANDOM

# from random import randint


# bilangan = []
# # mengenerate 5 bil bulat 0 s/d 10
# for i in range(10):
#     bil = randint(0, 100)
#     bilangan.append(bil)

# print(bilangan)
# print('Bilangan ke-6 adalah {}'.format(bilangan[5]))
# print(1 in bilangan)

# import random
# def cek_number_in_list(l,number):
#     position = 0
#     step = 0
#     for i in range(len(l)):
#         step=+1
#         if number == l[i]:
#             position = i+1
#     return position, step

# n = int(input('Masukkan banyak element list\t: '))


# list = []
# for i in range(10):
#     list.append(random.randint(1,100))

# print(list)

# number = int(input("Masukkan bilangan yang akan anda cari\t: "))
# position, step = cek_number_in_list(list, number)

# print("Bilangan yang anda cari ada di posisi\t: {}".format(position))
# print("Banyaknya langkah dalam pencarian\t: {}".format(step))



#BILANGAN PRIMA

def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima

print(cari_bilangan_prima(1, 40))

# def isPrime(n, step):
#     step+=1
#     if(n<2):
#         return False,step
#     for i in range(2,int(n)):
#         step+=1
#         if(n%i == 0):
#             return False, step
#     return True, step

# number = int(input("Masukkan bilangan\t: "))
# is_prime, step =isPrime(number,0)
# if is_prime:
#     print("{} adalah bilangan Prima".format(number))
# else:
#     print("{} bukan bilangan Prima".format(number))

# print("Banyaknya Langkah yang dibutuhkan\t: {}".format(step))







# #RANDOM PENGURUTAN
# from random import randint
# def proses(n):
#     bil = [ ]
#     for i in range(1,n+1):
#         bil.append(randint(1,100))
    
#     for i in range(0, n):
#         print (bil[i], end=" ")
#     print(" ")

#     #proses pengurutan
#     for i in range(0,n):
#         for j in range(0,n):
#             if(bil[i]<bil[j]):
#                 tmp = bil[i]
#                 bil[i] = bil[j]
#                 bil[j] = tmp
    
#     # menampilkan setelah urut
#     for i in range(0,n):
#         print(bil[i], end=" ")
# proses(5)


# import random
# def mysort(l,step):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             step+=1
#             if(l[i]<l[j]):
#                 tmp = l[i];l[i] = l[j];l[j] = tmp

# n = int(input("Masukkan banyak elemen list\t: "))
# list=[]

# for i in range(n):
#     list.append(random.randint(1,100))


# print('List sebelum urut',list)

# list_urut, step =  mysort(list,0)
# print('List setelah urut', list_urut)
# print("Langkah yang dibutuhkan untuk mengurutkan\t: {}".format(step))