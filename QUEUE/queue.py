class Queue:
    def __init__(self):
        self.items = []
        # self.max = n

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)


# q = Queue()
# print(q.is_empty())
# q.enqueue(4)
# q.enqueue('anjing')
# q.enqueue(True)
# print(q.size())
# print(q.is_empty())
# print(q.items())
# print(q.dequeue())
# print(q.items)


# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()
# print(q.items)

