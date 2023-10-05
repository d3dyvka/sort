import random

N = int(input())


def gen():
    a = list()
    N = int(input())
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


a = gen()
print(sort(a))


