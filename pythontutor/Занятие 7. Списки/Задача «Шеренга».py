a = input().split()
b = int(input())
a = list(map(int, a))
a.append(b)
a.sort()
a = a[::-1]
for i in range(len(a) - 1, -1, -1):
    if a[i] == b:
        print(i + 1)
        break
