def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / a * power(a, n + 1)
    elif n > 0:
        return a * power(a, n - 1)


c = float(input())
d = int(input())
print(power(c, d))