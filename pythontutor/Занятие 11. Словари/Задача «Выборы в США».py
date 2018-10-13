n = int(input())
d = {}
s = set()
l = []
for i in range(n):
    k, v = input().split()
    l += [[k, v]]
    s.add(k)
for i in s:
    d[i] = 0
for i in l:
    d[i[0]] += int(i[1])
out = []
for k,v in d.items():
    out += [[k,v]]
out.sort()
for i in out:
    print(i[0], i[1])