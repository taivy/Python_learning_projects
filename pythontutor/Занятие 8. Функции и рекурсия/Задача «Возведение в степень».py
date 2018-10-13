def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


c = float(input())
d = int(input())
print(power(c, d))