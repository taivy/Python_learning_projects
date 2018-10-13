
# insert
a = input().split()
k, c = input().split()
b = [i for i in a]
b.insert(int(k), c)
print(*b)

# v. 2
a = input().split()
k, c = input().split()
b = [i for i in a]
b.append(0)
for i in range(int(k), len(a)):
    b[i + 1] = a[i]
b[int(k)] = c
print(*b)