a = [i for i in input().split()]
b = input()
if b not in a:
    print('Отсутствует')
else:
    for i in range(len(a)):
        if a[i] == b:
            print(i, end=' ')