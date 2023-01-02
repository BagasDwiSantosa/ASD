def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-i):
            print('data[',j,']<data[',(j+1),']')
            if(data[j]>data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
    return data

from random import randint
dt = [randint(1,100) for i in range(10)]
print(dt)
dt_urut = bubble_sort(dt)
print(dt_urut)