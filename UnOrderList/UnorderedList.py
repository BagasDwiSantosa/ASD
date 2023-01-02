from unorder import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def append(self,item):
        temp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(temp)

    def pop(self):
        current = self.head
        if current == None:
            return -1
        else:
            while current.getNext() != None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            return current.getData()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def show(self):
        current = self.head
        # print('Head ->', end='')
        while current != None:
            print(current.getData())
            current = current.getNext()
        # print('None')

    # def append(self, item):
    #     temp = Node(item)
    #     if self.head == None:
    #         self.head = temp
        
    #     else:
    #         current = self.tail
    #         current.setNext(temp)
    #     self.tail = temp

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


isi = UnorderedList()

isi.add(10)
isi.add(11)
isi.add(12)
isi.add(13)
isi.add(14)
isi.add(15)
isi.add(16)

# print(isi.size())
# print(isi.search(10))
# print(isi.search(100))

# isi.add(16)
# print(isi.search(16))
# print(isi.size())

# isi.remove(10)
# print(isi.size())
# isi.remove(12)
# print(isi.size())
# isi.remove(15)
# print(isi.size())
# print(isi.search(12))
# print(isi.search(1000))
# print(isi.pop())
# print(isi.search(1000))


print("Sebelum dibalik :")
print(isi.show())
isi.reverse()
print('\nSetelah dibalik :')
print(isi.show())