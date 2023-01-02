from program import *

data_barang = []
pilih = menu()

while pilih in[i for i in range(1,6)]:
    if pilih == 1:
        tampil_data(data_barang)
    elif pilih == 2:
        barang = tambah_data()
        data_barang.append(barang)
    elif pilih == 3:
        edit_data(data_barang)
    pilih = menu()
