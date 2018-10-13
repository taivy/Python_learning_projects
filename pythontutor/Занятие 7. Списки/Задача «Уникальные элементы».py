a = input().split()
s = {i for i in a}
l = []
for i in s:
    n = a.count(i)
    if n == 1:
        l += [i]
print(*l)