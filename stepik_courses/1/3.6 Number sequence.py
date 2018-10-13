a = int(input())
b = []
c = 1
while len(b) < a:
    if b.count(c) < c:
        b += [c]
    else:
        c += 1
print(*b)