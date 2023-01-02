
from queue import Queue

def tampil_menu() :
    print('Simulasi Antrian')
    print('1. Masukkan Item ke Antrian')
    print('2. Hapus data dari Antrian')
    print('3. Tampilkan Antrian')
    print('4. Keluar Program')

    pilih = int(input('Masukkan pilihan :'))
    return pilih

q = Queue()
pilih= tampil_menu()
while(pilih != 4 ): 
    if pilih == 1:
        data = input('Masukkan item data : ')
        q.enqueue(data)
        if(q.is_full):
            print('Antrian sudah penuh')
    elif pilih == 2:
        q.dequeue()
    elif pilih == 3:
        print(q.items)
    elif pilih == 4:
        print('Keluar Program')
    else:
        print('Pilihan Anda Salah')


while(pilih in range(7)):
# while(not q.is_full()):
    n = input("Masukkan item ")
    q.enqueue(n)
    


