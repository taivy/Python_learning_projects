with open('dataset_3363_3.txt') as inf:
    l = []
    for s in inf:
        s = s.lower().strip().split()
        for i in s:
            l.append(i)
    d = {}
    s = set()
    for i in l:
        s.add(i)
    for i in s:
        cnt = 0
        for j in range(len(l)):
            if l[j] == i:
                cnt += 1
            d[i] = cnt
m = 0
for key in d.keys():
    a = d[key]
    if d[key] >= m:
        m = d[key]
lmax = []
for key in d.keys():
    if d[key] == m:
        lmax.append(key)
n = lmax[0]
for i in lmax:
    if str(i) < str(m):
        n = i
s = str(n) + ' ' + str(m)
print(s)
with open('dataset_3363_2.txt', 'w') as ouf:
    ouf.write(s)