from stack import Stack
# teks =input('\nMasukan parantheses : ')
# tumpukan = Stack()
# hasil = 'balance'
# for i in teks:
#     if(i=="("):
#         tumpukan.push(i)
#     else:
#         if(tumpukan.is_empty()):
#             hasil='No Balance'
#             break
#         else:
#             tumpukan.pop()
# if(not tumpukan.is_empty()):
#     hasil = 'No Balance'
# print(hasil)

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
while index < len(symbol_string) and balanced:
    symbol = symbol_string[index]
    if symbol == "(":
        s.push(symbol)
    else:
        if s.is_empty():
            balanced = False
        else:
            s.pop()
            index = index + 1
            if balanced and s.is_empty():
                return True
                