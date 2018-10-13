# вывод в консоль
d = {}
with open('dataset_3380_5.txt', 'r') as inf:
    for s in inf:
        a = s.strip().split('\t')
        d[a[0]] = []
with open('dataset_3380_5.txt', 'r') as inf:
    for s in inf:
        a = s.strip().split('\t')
        d[a[0]] += [int(a[2])]
for i in range(11):
    n = str(i + 1)
    print(n, end=' ')
    if n in d.keys():
        s = 0
        for j in d[n]:
            s += j
        s = s / len(d[n])
        print(s)
    if n not in d:
        print('-')

# вывод в файл
d = {}
with open('dataset_3380_5.txt', 'r') as inf:
    for s in inf:
        a = s.strip().split('\t')
        d[a[0]] = []
with open('dataset_3380_5.txt', 'r') as inf:
    for s in inf:
        a = s.strip().split('\t')
        d[a[0]] += [int(a[2])]
with open('dataset_3380_5.txt', 'w') as ouf:
    for i in range(12):
        n = str(i + 1)
        ouf.write(n + ' ')
        if n in d.keys():
            s = 0
            for j in d[n]:
                s += j
            s = s / len(d[n])
            ouf.write(str(s) + '\n')
        if n not in d:
            ouf.write('-\n')