from Stack import Stack

def rev_string():
    for i in kalimat:
        s.push(i)
    print('Kata/Kalimat setelah dibalik : ', end="")

    while(not s.is_empty()):
        print(s.pop(), end="")


s = Stack()
kalimat = input('Masukan kata/kalimat : ')
rev_string()

# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# m = Stack()
# print(m.push('x'))
# print(m.push('y'))
# print(m.pop())
# print(m.push('z'))
# print(m.peek())


# m = Stack()
# # m.push('k')
# m.push('x')
# m.push('y')
# m.push('z')
# while not m.is_empty():
#     m.pop()


