n = int(input())
z = [[0 for i in range(n)] for j in range(n)]
c = 1
x = 0
y = 0
u = 0
while u <= n ** 2:
    a = x
    b = n - 1 - x
    i = a
    for j in range(y, n - y):
        z[i][j] = c
        c += 1
    j = b
    for i in range(y + 1, n - y):
        z[i][j] = c
        c += 1
    i = b
    for j in range(n - 2 - y, y, -1):
        z[i][j] = c
        c += 1
    j = a
    for i in range(n - 1 - y, y, -1):
        z[i][j] = c
        c += 1
    x += 1
    y += 1
    u += 1
for i in z:
    for j in i:
        print(j, end=' ')
    print()