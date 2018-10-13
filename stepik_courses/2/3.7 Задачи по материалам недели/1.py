a = int(input())
d = {}
ls = []
for i in range(a):
    s = input().split(';')
    ls.append(s)
    d[s[0]] = [0 for i in range(5)]
    d[s[2]] = [0 for i in range(5)]
s = 0
for i in d.keys():
    for j in ls:
        if i in j:
            s += 1
        d[i][0] = s
    s = 0
for i in ls:
    key1 = i[0]
    key2 = i[2]
    if i[1] > i[3]:
        d[key1][1] += 1
        d[key2][3] += 1
    elif i[1] == i[3]:
        d[key1][2] += 1
        d[key2][2] += 1
    elif i[1] < i[3]:
        d[key2][1] += 1
        d[key1][3] += 1
for key in d.keys():
    s = (d[key][1] * 3) + d[key][2]
    d[key][4] = s
for key, value in d.items():
    print(key + ': ', end = '')
    print(*value, end=' ')
    print()