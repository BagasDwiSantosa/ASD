def menu():
    print('Pilih menu yang anda inginkan')
    print('==============================')
    print('1 : Tampil data')
    print('2 : Tambah data')
    print('3 : Edit data ')
    print('4 : Hapus data')
    print('5 : Tampil data urut')
    print('6 : Keluar Program')

    inputan = int(input("Masukkan Pilihan anda : "))
    return inputan

def tampil_data(data):
    print('Daftar Barang')
    print('-'*83)
    print('| Kode Barang |            Nama Barang            | QTY | Harga Beli | Harga Jual |')
    print('-'*83)

    if(len(data)==0):
        print('|'+' '*28+'Data Barang Masih Kosong'+' '*29+'|')
    else:
        for barang in data :
            print('|'+barang['kode'].ljust(13," ")+'|'+barang['nama'].ljust(35,' ')+'|'+barang['qty'].center(5,' ')+'|'+barang['harga_beli'].rjust(12,' ')+'|'+barang['harga_jual'].rjust(12,' ')+'|')
    print('-'*83)
    input('Tekan enter untuk lanjut!')


def tambah_data():
    kode = input("Kode Barang\t: ")
    nama = (input('Nama Barang\t: '))
    qty = input("QTY\t\t: ")
    harga_beli = input('Harga Beli\t: ')
    harga_jual = input('Harga Jual\t: ')

    barang = {'kode':kode, 'nama':nama, 'qty':qty,'harga_beli':harga_beli,'harga_jual':harga_jual}
    return barang

def edit_data(data):
    tampil_data(data)
    kode = input("Masukkan Kode dari data barang yang akan diEdit : ")

    ketemu = False
    posisi = -1
    for barang in data:
        posisi+=1
        if kode ==barang['kode']:
            ketemu = True
            data[posisi]['harga_beli'] = input('Harga Beli Baru : ')
            data[posisi]['harga_jual'] = input('Harga Jual Baru : ')
            break
        elif not ketemu:
            print("Kode tidak ditemukan")

    