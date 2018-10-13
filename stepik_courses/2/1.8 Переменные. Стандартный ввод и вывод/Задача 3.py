x = int(input())
h = int(input())
m = int(input())
m1 = (h * 60) + m + x
h2 = m1 // 60
m2 = m1 % 60
print(h2)
print(m2)