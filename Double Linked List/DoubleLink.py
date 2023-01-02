class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def add(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.next

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return self.start_node
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break 
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

double = DoublyLinkedList()

double.add(10)
double.add(11)
double.add(12)
double.add(13)
double.add(14)

double.add_end(15)
print(double.traverse_list())

double.insert_before_item(10, 10000)
print(double.traverse_list())

