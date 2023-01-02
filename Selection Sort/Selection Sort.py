def urutTurun(a, n):
    for i in range(0,n-1):
        for j in range(i+1, n-1):
            if(a[i]<a[j]):
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    
    return a


data = [9,6,3,1,4]
n = 5
data1 = urutTurun(data, n)



A = [64,25,12,22,16,18,19,100]

for i in range(len(A)):
    maxx = i
    for j in range (i+1, len(A)):
        if A[maxx] > A[j]:
            maxx = j

    A[i], A[maxx] = A[maxx], A[i]
    print("looping ke %s"%(i), A)

print("\nsorted array = ", A)