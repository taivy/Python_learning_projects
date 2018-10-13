a = float((input()))
b = float((input()))
c = input()
if c == '+':
    d = a + b
    d = float(d)
    print(d)
elif c == '-':
    d = a - b
    d = float(d)
    print(d)
elif c == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        d = a / b
        d = float(d)
        print(d)
elif c == '*':
    d = a * b
    d = float(d)
    print(d)
elif c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        d = a % b
        d = float(d)
        print(d)
elif c == 'pow':
    d = a ** b
    d = float(d)
    print(d)
elif c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        d = a // b
        d = float(d)
        print(d)
