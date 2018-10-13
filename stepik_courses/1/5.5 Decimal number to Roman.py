a = int(input())
s = ''
d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: "C", 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
c = a
for j in 1000, 500, 100, 50, 10, 5, 1:
    b = c // j
    e = c - c % j
    f = int(str(c)[0]) * 10 ** (len(str(c)) - 1)
    if str(f)[0] == '9' or str(f)[0] == '4':
        r = d[f]
        c -= f
    else:
        r = d[j] * b
        c -= b * j
    s += r
print(s)