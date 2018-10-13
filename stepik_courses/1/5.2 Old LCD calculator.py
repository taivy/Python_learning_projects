a = input()
d = {}
for i in range(10):
    d[i] = ''
for row in range(1, 8):
    d[row] += '|'
for row in 0, 8:
    d[row] += 'x'
d2 = {}
for i in range(10):
    d2[i] = ['    ' for i in range(7)]
for i in 0, 2, 3, 5, 6, 8, 9:
    d2[i][0] = ' -- '
    d2[i][6] = ' -- '
for i in 0, 8:
    for j in 1, 2, 4, 5:
        d2[i][j] = '|  |'
for i in 1, 3, 4, 7, 9:
    for j in 1, 2, 4, 5:
        d2[i][j] = '   |'
for i in 2, 3, 4, 5, 8, 9:
    d2[i][3] = ' -- '
a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '
d2[7][0] = a1
d2[2][1] = a4
d2[2][2] = a4
d2[2][4] = a5
d2[2][5] = a5
d2[4][1] = a2
d2[4][2] = a2
d2[5][1] = a5
d2[5][2] = a5
d2[5][4] = a4
d2[5][5] = a4
d2[6] = [a1, a5, a5, a1, a2, a2, a1]
d2[9][1] = a2
d2[9][2] = a2
for i in a:
    for row in 0, 8:
        d[row] += '-----'
    for row in range(1, 8):
        d[row] += d2[int(i)][row - 1]
        d[row] += ' '
for row in range(1, 8):
    d[row] += ' '
    d[row] += '|'
for row in 0, 8:
    d[row] += '-x'
for i in d:
    print(d[i], end='')
    print()

