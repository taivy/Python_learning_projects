a = input().split()
a = list(map(int, a))
b = [a[i] for i in range(len(a))]
for i in range(0, len(a) - 1, 2):
    b[i+1] = a[i]
    b[i] = a[i+1]
print(*b)