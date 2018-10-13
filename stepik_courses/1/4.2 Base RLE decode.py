a = input()
s = ''
n = 0
l = ['' for i in range(0, len(a) * 2)]
for i in range(len(a)):
    try:
        b = int(a[i])
    except ValueError:
        n += 1
        l[n] = a[i]
        n += 1
    else:
        l[n] += a[i]
for i in range(len(l)):
    if l[i] == '':
        l[i] = '1'
for i in range(0, len(l), 2):
    try:
        b = int(l[i + 1])
    except ValueError:
        print(int(l[i]) * l[i+1], end='')