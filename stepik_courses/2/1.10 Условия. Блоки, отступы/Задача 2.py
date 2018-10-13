y = int(input())
if y % 4 == 0 and y % 100 != 0:
	print('Високосный')
elif y % 400 == 0:
	print('Високосный')
else:
	print('Обычный')

