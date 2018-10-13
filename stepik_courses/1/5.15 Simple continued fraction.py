a, b = input().split('/')
a = int(a)
b = int(b)
l = []
while b != 0:
    c = a // b
    d = a % b
    a = b
    b = d
    l.append(c)
print(*l)