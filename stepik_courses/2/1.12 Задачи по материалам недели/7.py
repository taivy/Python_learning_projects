a = int(input())
a1 = a // 100000
a6 = a % 10
a2 = (a // 10000) - (a1 * 10)
a1a2 = str(a1) + str(a2)
a3 = (a // 1000) - (int(a1a2) * 10) # можно было так: a3 = (a // 100) - a1 * 100 - a2 * 10
a5 = (((a % 100) - a6) // 10)
a4 = (((a % 1000) - a5) // 100)
if a1 + a2 + a3 == a4 + a5 + a6:
    print('Счастливый')
else:
    print('Обычный')