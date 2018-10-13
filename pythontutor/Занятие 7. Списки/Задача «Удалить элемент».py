a = input().split()
k = int(input())
b = [i for i in a]
for i in range(k, len(a) - 1):
    b[i] = a[i+1]
b[len(a) - 1] = a[k]
b.pop()
print(*b)