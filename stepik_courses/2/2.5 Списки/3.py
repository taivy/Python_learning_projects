a = [int(i) for i in input().split()]
min = min(a)
max = max(a) + 1
for i in range(min, max):
    if a.count(i) > 1:
        print(i, end=' ')