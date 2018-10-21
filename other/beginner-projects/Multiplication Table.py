from itertools import chain

def table(size):
    rows = [[i*j for j in range(1, size+1)] for i in range(1, size+1)]
    flattened = chain.from_iterable(rows)
    max_n = max(flattened)
    frmtd = []
    for row in rows:
        frmtd.append(list(map(str, row)))
    for row in frmtd:
        for i in range(len(row)):
            while len(row[i]) < len(str(max_n)) + 1:
                new = row[i] + ' '
                row[i] = new
    for row in frmtd:
        print(''.join(row))


print('Enter size of the table')
size = int(input())
table(size)




