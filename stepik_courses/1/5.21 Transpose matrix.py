rows, cols = input().split()
m = [[0 for i in range(int(rows))] for j in range(int(cols))]
d = {}
for i in range(int(rows)):
    row = input().split()
    for j in range(len(row)):
       row[j] = int(row[j])
    d[i] = row
for i in d:
    for j in range(int(cols)):
        m[j][i] = d[i][j]
for i in m:
    for j in i:
        print(j, end=' ')
    print()