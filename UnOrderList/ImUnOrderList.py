mylist = UnorderedList()
def tampil_menu() :
    print('Simulasi Antrian')
    print('1. Masukkan Data')
    print('2. Mengukur Data')
    print('3. Mencari Data')
    print('4. Mengecek Data')
    print('5. Menghapus Data')
    print('6. Keluar Program')

    pilih = int(input('Masukkan pilihan :'))
    return pilih


while True: 
    pilih= tampil_menu()
    if pilih == 1 :
        data = input('Masukkan data : ')
        mylist.add(data)
   

    elif pilih == 2:
        print(mylist.size())

    elif pilih == 3:
        cari = input('Masukkan data : ')
        print(mylist.add(cari))      

    elif pilih == 4:
        print(mylist.is_empty())

    elif pilih == 5:
        hapus = input('Masukkan data yang dihapus : ')
        print(mylist.remove(hapus))    
    else:
        print('KELUAR BOSSS')