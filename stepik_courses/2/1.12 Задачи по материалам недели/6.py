a = int(input())
b = a % 10
c = a % 100
if 11 <= c <= 19:
    a = str(a)
    print(a + ' программистов')
else:
    if b == 1:
        a = str(a)
        print(a + ' программист')
    elif 2 <= b < 5:
        a = str(a)
        print(a + ' программиста')
    elif 5 <= b <= 9:
        a = str(a)
        print(a + ' программистов')
    elif b == 0:
        a = str(a)
        print(a + ' программистов')

