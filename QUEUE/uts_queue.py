from queue import Queue

def tampil_menu() :
    print('Menu Antrian Bagas DS')
    print('1. Masukkan Data ke Antrian')
    print('2. Hapus Data dari Antrian')
    print('3. Tampilkan Data Antrian')
    print('4. Keluar Program')

    pilihan = int(input('Masukkan pilihan menu :'))
    return pilihan

q = Queue()

while True:
    print()
    pilihan= tampil_menu()
    if pilihan == 1:
        masukan = input("Masukkan Data\t: ")
        q.enqueue(masukan)

    elif pilihan == 2:
        q.dequeue()
    
    elif pilihan == 3 :
        print('\n ====== Data Antrian =====')
        print(q.items)
        print()
    
    elif pilihan == 4:
        print('Keluar')
        break

    else:
        print('Ada Kesalahan')



