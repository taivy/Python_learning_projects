a = input().split()
a = map(int, a)
for i in a:
    if i % 2 == 0:
        print(i, end=' ')
