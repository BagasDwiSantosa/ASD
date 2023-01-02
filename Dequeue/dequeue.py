class Dequeue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        return self.items.append(item)

    def add_rear(self, item):
        return self.items.insert(0, item)     
    
    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Dequeue()

# print(d.is_empty())
# d.add_front('halo dek')
# d.add_front('heloooo')
# d.add_rear('kuliah dimana dek')
# d.remove_front()
# d.remove_rear()
# print(d.size())
# print(d.items)
