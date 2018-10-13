b = input()
a = b.upper()
l = len(a)
n = a.count('G') + a.count('C')
p = n / l * 100
print(float(p))