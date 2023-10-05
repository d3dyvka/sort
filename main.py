import random
import time

N = int(input())
f = open('out.txt', 'w')


def gen():
    a = list()
    for i in range(N):
        a.append(random.randint(1, 20))
    return a


def buble(a):

    for j in range(N - 1):
        for i in range(N - j - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


def sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
            a[i], a[m] = a[m], a[i]
    return a

def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        L =[]
        M = []
        K = []
        for elem in a:
            if elem < q:
                L.append(elem)
            elif elem > q:
                K.append(elem)
            else:
                M.append(elem)
    return quick_sort(L) + M + quick_sort(K)


a = gen()

start = time.time()
buble(a)
end = (time.time() - start)
print(end, file=f)

start = time.time()
sort(a)
end1 = (time.time() - start)
print(end1, file=f)

start2 = time.time()
quick_sort(a)
end2 = (time.time() - start2)
print(end2, file=f)