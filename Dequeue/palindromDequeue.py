from dequeue import Dequeue

def pal_checker(a_string):
    char_dequeue = Dequeue()

    for ch in a_string:
        char_dequeue.add_rear(ch)

    still_equal = True

    while char_dequeue.size() > 1 and still_equal:
        first = char_dequeue.remove_front()
        last = char_dequeue.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

str = input('Masukan string : ')
if(pal_checker(str)):
    print(str, ' palindrom')
else:
    print(str, ' tidak palindrom')