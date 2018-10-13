a = input().split('_')
for n in range(len(a)):
    print(a[n][0].upper() + a[n][1::], end='')