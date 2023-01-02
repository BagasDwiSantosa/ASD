# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('cat')
# # print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def push(self,item):
#         self.items.insert(0,item)
#     def pop(self):
#         return self.items.pop(0)
#     def peek(self):
#         return self.items[0]
#     def size(self):
#         return len(self.items)

# s = Stack()
# s.push('hello')
# s.push('true')
# print(s.pop())

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)

s = Stack()
kalimat = input('Masukan kata/kalimat : ')

for i in kalimat:
    s.push(i)
print('Kata/Kalimat setelah dibalik : ', end="")

while(not s.is_empty()):
    print(s.pop(), end="")