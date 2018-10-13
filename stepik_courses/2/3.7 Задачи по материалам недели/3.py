a = int(input())
ld = []
for i in range(a):
    w = input().lower()
    ld += [w]
b = int(input())
lt = []
for i in range(b):
    w = input().lower().split()
    lt += [w]
s = set()
for i in lt:
    for j in i:
        if j not in ld:
            s.add(j)
for i in s:
    print(i)