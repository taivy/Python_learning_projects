
print('Enter total weight of each type of coin you have (pennies, nickels, dimes, and quarters) respectively, comma '
      'separates, without whitespaces')

while True:
    try:
        inp = input()
        pw, nw, dw, qw = inp.split(',')
        break
    except ValueError:
        print('Incorrect input')
        continue

to_int = [pw, nw, dw, qw]
pw, nw, dw, qw = list(map(int, to_int))

coins = ['p', 'n', 'd', 'q']
names = {'p': 'Penny', 'n': 'Nickel', 'd': 'Dime', 'q': 'Quarter'}

user_weights = {'p': pw, 'n': nw, 'd': dw, 'q': qw}
weights = {'p': 2.50, 'n': 5, 'd': 2.268, 'q': 5.67}
wrappers = {'p': 50, 'n': 40, 'd': 50, 'q': 40}

cnt = {coin: round(user_weights[coin] // weights[coin]) for coin in coins}
wrap = {coin: round(cnt[coin] / wrappers[coin]) for coin in coins}

print('Wrappers: ')
for coin in wrap.keys():
    print(names[coin] + ': ' + str(wrap[coin]))

print('\nCoins: ')
for coin in wrap.keys():
    print(names[coin] + ': ' + str(cnt[coin]))



