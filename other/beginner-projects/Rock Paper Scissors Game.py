from random import choice

variants = ['r', 'p', 's']
beats = {'r':'s', 'p':'r', 's':'p'}

while True:
    print('Pick rock, paper or scissors (by entering r, p or s)')
    user_choice = input()
    if user_choice != 'r' and user_choice != 'p' and user_choice != 's':
        print('Incorrent choice')
        continue
    computer_choice = choice(variants)
    print('Computer choice: ' + computer_choice)

    if beats[user_choice] == computer_choice:
        print('User wins')
    elif beats[computer_choice] == user_choice:
        print('Computer wins')
    elif user_choice == computer_choice:
        print('Draw')

    print('Play again? (Y/N)')
    play = input()
    if play == 'Y':
        continue
    elif play == 'N':
        break




