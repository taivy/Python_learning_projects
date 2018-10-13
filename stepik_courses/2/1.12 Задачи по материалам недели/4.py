f = input()
if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    d = p * (p - a) * (p - b) * (p - c)
    s = float(d ** 0.5)
    print(s)
elif f == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
elif f == 'круг':
    r = int(input())
    s = 3.14 * r ** 2
    print(s)
