b = 1
while b == 1:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)