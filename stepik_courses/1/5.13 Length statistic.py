# вариант 1
s = input().split()
d = {}
for i in s:
    d[len(i)] = 0
for i in s:
    d[len(i)] += 1
for key in range(0, max(d) + 1):
    if d.get(key) != None:
        print(str(key) + ': ' + str(d.get(key)))

# вариант 2
s = input().split()
d = {}
l = []
for i in s:
    d[len(i)] = 0
for i in s:
    d[len(i)] += 1
for k in d.keys():
    l += [k]
l.sort()
for i in l:
    print(str(i) + ': ' + str(d.get(i)))

