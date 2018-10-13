a = input().split()
a = list(map(int, a))
b = [a[i] for i in range(len(a))]
b[a.index(max(a))] = min(a)
b[a.index(min(a))] = max(a)
print(*b)