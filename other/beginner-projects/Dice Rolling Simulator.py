from random import randint


print('This is simulation of dice rolls. You can roll a dice with any amount of sides any times and see, how many times'
      ' each side appeared and percentage it appeared.', end='\n\n')

while True:
    try:
        print('Enter sides: ')
        sides = int(input())
        print('Enter number of rolls: ')
        rolls = int(input())
        break
    except ValueError:
        print('Enter correct numbers')
        continue

cnt = {i:0 for i in range(1, sides+1)}

for i in range(rolls):
    num = randint(1, sides)
    cnt[num] += 1

print('\nHow many times each number came up:')
i = 0
for num in cnt.keys():
    if i == len(cnt.keys()) - 1:
        print(str(num) + ': ' + str(cnt[num]))
    else:
        print(str(num) + ': ' + str(cnt[num]), end=', ')
    i += 1

percents = {num: round(times/rolls, 4)*100 for num, times in cnt.items()}
print('\nPercentage:')
i = 0
for num in percents.keys():
    if i == len(percents.keys()) - 1:
        print(str(num) + ': ' + str(percents[num]) + '%')
    else:
        print(str(num) + ': ' + str(percents[num]) + '%', end=', ')
    i += 1
