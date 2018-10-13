a = input().split()
a = list(map(int, a))
a.sort()
s = 1
for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        s += 1
print(s)