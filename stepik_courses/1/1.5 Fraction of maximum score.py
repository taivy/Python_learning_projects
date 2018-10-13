a = input().split()
s = 0
for i in a:
    if i == 'A':
        s += 1
result = round(s / len(a), 2)
print('{0:.2f}'.format(result))