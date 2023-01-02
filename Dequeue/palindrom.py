from dequeue import Dequeue

# def palindrom_checker(string):
#     d = Dequeue()
#     d.add_front(string)
#     is_palindrom = True
#     print(d.items)
#     while d.size() > 1 and is_palindrom:
#         depan = d.remove_front()
#         belakang = d.remove_rear()
#         is_palindrom = depan == belakang

# palindrom_checker('aku')



def palindrom_checker(string):
    char_dequeue = Dequeue(len(string))
    for ch in string:
        char_dequeue.add_rear(ch)
    
    is_palindrom = True
    while char_dequeue.size() > 1 and is_palindrom:
        first = char_dequeue.remove_front()
        last = char_dequeue.remove_rear()
        is_palindrom = (first == last)

    return is_palindrom


# string = input("Masukkan string\t: ")

print(palindrom_checker('string'))
