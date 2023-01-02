class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
class DoublyLink:
    head = None
    tail = None        
    def ikitambah(self):
        temp = int(input('Masukkan data baru : '))
        new_node = Node(temp)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
   
    def ikihapus(self):
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
            
    def ikinampilno(self):
        print ("Tampilkan list data:")
        current_node = self.head

        while current_node is not None:
            print (current_node.data),
            current_node = current_node.next
             
    def ikimenune(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
          
            print('Pilih menu')
            print('==============================')
            print('1 : Tambah data')
            print('2 : Hapus data')
            print('3 : Tampilkan data')
            print('4 : Keluar')

            pilihan = str(input("Masukkan Menu yang anda pilih : "))
            if(pilihan == "1"):
                self.ikitambah()
            elif(pilihan == "2"):
                self.ikihapus()
            elif(pilihan == "3"):
                self.ikinampilno()
                x = input("")
            else :
                pilih ="n"
               
if __name__ == "__main__":
    d = DoublyLink()
    d.ikimenune()