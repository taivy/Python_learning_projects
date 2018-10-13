def f(n):
    nums_list = []
    while n != 1:
        d = 2
        while True:
            if n % d == 0:
                nums_list += [d]
                n = n / d
                break
            else:
                d += 1
    return nums_list

a = int(input())
b = f(a)
print(b)