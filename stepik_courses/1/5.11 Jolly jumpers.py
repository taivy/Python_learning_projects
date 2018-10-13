a = input().split()
is_jolly = True
b = []
for i in range(len(a) - 1):
    n = int(a[i]) - int(a[i+1])
    if n < 0:
        n = 0 - n
    b.append(n)
for i in range(1, len(a) - 1):
    if i not in b:
        is_jolly = False
if is_jolly:
    print('Jolly')
else:
    print('Not jolly')