import random

a = list()
N = int(input())

for i in range(N):
    a.append(random.randint(1, 20))

print(a)

for j in range(N - 1):
    for i in range(N - j - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)



