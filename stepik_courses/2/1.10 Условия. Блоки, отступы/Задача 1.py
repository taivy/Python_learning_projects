a = int(input())
b = int(input())
h = int(input())
if h < a:
	print('Недосып')
elif h > b:
	print('Пересып')
else:
	print('Это нормально')