
menu = """
1. Chicken Strips - $3.50
2. French Fries - $2.50
3. Hamburger - $4.00
4. Hotdog - $3.50
5. Large Drink - $1.75
6. Medium Drink - $1.50
7. Milk Shake - $2.25
8. Salad - $3.75
9. Small Drink - $1.25"""

prices = {'1': 3.50, '2': 2.50, '3': 4.00, '4': 3.50,
          '5': 1.75, '6': 1.50, '7': 2.25, '8': 3.75, '9': 1.25}

print(menu)
print('Enter order (i.e. if one large drink, two small drinks, two hamburgers, one hotdog, and a salad, '
      'you should type in 5993348)')
order = input()

price = 0
for meal in order:
    price += prices[meal]

print('Price is ' + str(price) + '$')

