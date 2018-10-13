a = input().split()
a = list(map(int, a))
s = 0
for i in range(1, len(a) - 1):
    if a[i] > a[i + 1] and a[i] > a[i - 1]:
        s += 1
print(s)