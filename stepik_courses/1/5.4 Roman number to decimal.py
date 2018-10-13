a = input()
b = []
for i in a:
    if i == 'I':
        i = 1
    elif i == 'V':
        i = 5
    elif i == 'X':
        i = 10
    elif i == 'L':
        i = 50
    elif i == 'C':
        i = 100
    elif i == 'D':
        i = 500
    elif i == 'M':
        i = 1000
    b.append(i)
s = 0
for n in range(len(b) - 1):
    if b[n] < b[n + 1]:
        n = - b[n]
    else:
        n = b[n]
    s += n
s += b[len(b) - 1]
print(s)