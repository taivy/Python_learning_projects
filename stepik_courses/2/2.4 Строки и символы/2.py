a = input()
i = 0
j = 1
s = 1
if len(a) == 1:
    print(a[0] + str(1))
while 0 <= j < len(a) and 0 <= i < len(a):
    if j == len(a) - 1:
        if a[i] != a[j]:
            print(a[i] + str(s), end='')
            print(a[j] + str(1), end='')
        else:
            s += 1
            b = a[i:j]
            print(a[i] + str(s), end='')
        j += 1
    else:
        if a[i] != a[j]:
            b = a[i:j]
            print(a[i] + str(s), end='')
            i = j
            j += 1
            s = 1
        else:
            j += 1
            s += 1