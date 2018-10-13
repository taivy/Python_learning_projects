a = input().split()
s = set()
for i in a:
    if a.count(i) > 1:
        s.add(i)
print(*s)
