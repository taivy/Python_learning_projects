a = int(input())
n = 0
s = 0
e = 0
w = 0
for i in range(a):
    str = input().split()
    if str[0] == 'север':
        n += int(str[1])
    elif str[0] == 'юг':
        s += int(str[1])
    elif str[0] == 'восток':
        e += int(str[1])
    elif str[0] == 'запад':
        w += int(str[1])
x = e - w
y = n - s
print(x, y)