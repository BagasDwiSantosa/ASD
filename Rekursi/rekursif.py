#MENCETAK NILAI 1 SAMPAI N REKRUSIF

# def cetak(n):
#     print(n)
#     if (n > 1):
#         cetak(n-1)
# cetak(10)

# print('==============')

# def cetak(n,batas):
#     print(batas-n+1)
#     if (n > 1):
#         cetak(n-1,batas)
# cetak(10,10)



# n = int(input('Masukkan nilai n: '))

# def hitung_faktorial (n):
#   if n > 2:
#     return n * hitung_faktorial(n - 1)
#   return 2

# faktorial = hitung_faktorial(n)
# print(f'{n}! = {faktorial}')

#FIBONANCI REKRUSIF

# def fibonacci (n):
#   if n < 1:
#     return [n]

#   listSebelumN = fibonacci(n - 1)
#   angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
#   angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

#   return listSebelumN + [angka1 + angka2]

# panjang = int(input('Masukkan panjang deret:'))

# # kita kurangin satu agar tidak kelebihan :D
# print(fibonacci(panjang - 1))



#DESIMAL TO BINER REKRUSIF

# n = int(input('Input angka desimal: '))
 
# a = []
# i = 0
# while n > 0:
#   a.append(n % 2)
#   print(a)
#   n = n // 2
#   i = i+1
   
# print('Angka binernya adalah: ',end='')
 
# for i in range(i-1,-1,-1):
#   print(a[i],end='')

# def desimal_biner(n):
#     if n in [0,1]:
#         return str(n)
#     else:
#         sisa = n % 2
#         bagi = n//2
#         return desimal_biner(bagi)+str(sisa)

# print(desimal_biner(100))


# Recursive Python function to solve the tower of hanoi
 
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')

# A, C, B are the name of rod