class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
class DoublyLink:
    head = None
    tail = None        
    def add(self):
        temp = int(input('Masukkan data baru : '))
        new_node = Node(temp)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
   
    def remove(self):
        temp = int(input('Masukkan data yang akan dihapus : '))
        current_node = self.head

        while current_node is not None:
            if current_node.data == temp:
                if current_node.next is None:
                    current_node.prev.next = None
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next 
                    current_node.next.prev = None 

            current_node = current_node.next
            
    def show(self):
        print ("Tampilkan list data:")
        current_node = self.head

        while current_node is not None:
            print (current_node.prev.data) if hasattr(current_node.prev, "data") else None,
            print (current_node.data),
            print (current_node.next.data) if hasattr(current_node.next, "data") else None
            current_node = current_node.next
             
    def menu(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
          
            print('\nPilih menu dibawah ini :')
            print('==============================')
            print('1 : Tambah data ke linked list')
            print('2 : Hapus data di linked list')
            print('3 : Tampilkan data di linked list')
            print('4 : Keluar Program')

            pilihan = int(input("Masukkan Menu yang anda pilih : "))
            if(pilihan == 1):
                self.add()
            elif(pilihan == 2):
                self.remove()
            elif(pilihan == 3):
                self.show()
                x = input("")
            else :
                pilih ="n"
               
if __name__ == "__main__":
    d = DoublyLink()
    d.menu()