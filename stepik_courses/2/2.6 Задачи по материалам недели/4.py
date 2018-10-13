a = []
b = []
n = 0
k = input().split()
while k[0] != 'end':
    a += [0]
    b += [0]
    d = [int(i) for i in k]
    e = [int(i) for i in k]
    a[n] = d
    b[n] = e
    n += 1
    k = input().split()
m = len(a)
n = len(a[0])
for i in range(m):
    for j in range(n):
        sum = a[i - 1][j] + a[i - m + 1][j] + a[i][j - 1] + a[i][j - n + 1]
        b[i][j] = sum
for i in b:
    for j in i:
        print(j, end=' ')
    print()