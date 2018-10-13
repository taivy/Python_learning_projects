n = int(input())
a = []
for i in range(n + 1):
    for s in range(i):
        a.append(i)
b = [a[i] for i in range(n)]
for i in b:
    print(i, end=" ")