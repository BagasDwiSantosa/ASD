from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
        else :
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            # elif current.get_data() != item:
            #     found = False
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def show(self):
        current = self.head
        while current != None:
            print(current.get_data(), end = ',')
            current = current.get_next()


Unorder = UnorderedList()


print(Unorder.is_empty())
Unorder.add(10)
Unorder.add(11)
Unorder.add(12)
Unorder.add(13)
Unorder.add(14)
Unorder.add(15)

print(Unorder.size())
print(Unorder.search(10))
print(Unorder.search(100))

Unorder.add(16)
print(Unorder.search(16))
print(Unorder.size())

Unorder.remove(10)
print(Unorder.size())
Unorder.remove(12)
print(Unorder.size())
Unorder.remove(15)
print(Unorder.size())
print(Unorder.search(12))

print(Unorder.is_empty())

print(Unorder.show())
