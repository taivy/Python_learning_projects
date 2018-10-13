n = int(input())
d = {}
for i in range(n):
    v = int(input())
    if v in d:
        print(d[v])
    else:
        fv = f(v)
        print(fv)
        d[v] = fv