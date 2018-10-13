a = [i.lower() for i in input().split()]
s = set()
for i in a:
    s.add(i)
d = {}
for i in s:
    cnt = 0
    for j in range(len(a)):
        if i == a[j]:
            cnt += 1
        d[i] = cnt
for key, value in d.items():
    print(key, value)
