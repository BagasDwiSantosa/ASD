def bubble_sort(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


unordered = [5, 3, 4, 8, 1, 2, 9, 6]
print(bubble_sort(unordered))

from random import randint
dt = [randint(1,100) for i in range(10)]
print(bubble_sort(dt))