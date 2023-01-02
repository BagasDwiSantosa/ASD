def test():
    l = []
    for i in range(1000):
        l = l+[i]
    print(l)
test()




from timeit import Timer
t1 = Timer("text()", "from__main__import test1")
print("concat", t1.timeit(1000))



