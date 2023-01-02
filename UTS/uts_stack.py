class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)




def pal_checker(a_string):
    char_dequeue = Stack()

    for i in a_string:
        char_dequeue.push(i)

    still_equal = True

    while char_dequeue.size() > 1 and still_equal:
        first = char_dequeue.pop()
        last = char_dequeue.peek()
        if first != last:
            still_equal = False

    return still_equal

str = input('Masukkan string : ')
if(pal_checker(str)):
    print(str, ' palindrom')
else:
    print(str, ' tidak palindrom')
