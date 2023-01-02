
def merge_sort(list_bilangan):
  jumlah_bilangan =  len(list_bilangan)
  if jumlah_bilangan > 1:
    posisi_tengah = len(list_bilangan)//2
    potongan_kiri = list_bilangan[:posisi_tengah]
    potongan_kanan = list_bilangan[posisi_tengah:]
    
    merge_sort(potongan_kiri)
    merge_sort(potongan_kanan)

    jumlah_bilangan_kiri = len(potongan_kiri)
    jumlah_bilangan_kanan = len(potongan_kanan)
    c_all,c_kiri,c_kanan = 0,0,0 
    print('Sebelum merge:',list_bilangan)  
    print('Potongan sebelum merge:',potongan_kiri,':',potongan_kanan)
    while c_kiri < jumlah_bilangan_kiri and c_kanan < jumlah_bilangan_kanan:
      if potongan_kiri[c_kiri] < potongan_kanan[c_kanan]: 
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1

      else:
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      c_all = c_all + 1

    while c_kiri < jumlah_bilangan_kiri:
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
        c_all = c_all + 1

    while c_kanan < jumlah_bilangan_kanan:
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
        c_all = c_all + 1
    print('Setelah merge:', list_bilangan)
    print()
          
angka = [6,5,3,1,8,7,2,4]
# angka =[0,9,8,7,6,5,4,3,2,1]
print('Sebelum sort:',angka)
merge_sort(angka)
print('Setelah sort:',angka)

# animasi https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif




# a = [6,5,3,1,8,7,2,4]

# posisi_tengah = len(a)//2
# potongan_kiri = a[:posisi_tengah]
# potongan_kanan = a[posisi_tengah:]
# print(potongan_kiri)
# print(potongan_kanan)