def collatz(a):
    b = a
    while b != 1:
        if b % 2 == 0:
            b = b // 2
        elif b % 2 == 1:
            b = b * 3 + 1
        l.append(b)
c = int(input())
l = [c]
collatz(c)
print(*l)