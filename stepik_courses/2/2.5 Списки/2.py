a = [int(i) for i in input().split()]
b = []
c = len(a)
if len(a) == 1:
    print(a[0])
elif len(a) == 2:
    u = a[0] + a[1]
    print(u, u)
else:
    for i in range(c):
        n1 = i - 1
        if i == len(a) - 1:
            n2 = 0
        else:
            n2 = i + 1
        e1 = a[n1]
        e2 = a[n2]
        s = e1 + e2
        b += [s]
for i in b:
    print(i, end=" ")