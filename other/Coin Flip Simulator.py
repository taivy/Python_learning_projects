from random import choice

def flip(n):
    heads = 0
    tails = 0
    var = [1, 2]
    for i in range(n):
        coin_choice = choice(var)
        if coin_choice == 1:
            heads += 1
        else:
            tails += 1
    print('Орёл: ' + str(heads))
    print('Решка: ' + str(tails))


print('Enter number of flips: ')
n = int(input())
flip(n)