from random import randint

print('To win you need to guess the randomly selected number between 1 and 100. Enter your guess. '
      'If your answer is wrong, try another number.')

while True:
    guess = int(input())
    num = randint(1, 100)
    guesses = 1

    while guess != num:
        guesses += 1
        if guess > num:
            print('Your number is higher than answer')
            guess = int(input())
        elif guess < num:
            print('Your number is lower than answer')
            guess = int(input())

    print('Congratulations!')
    print('Guesses: ' + str(guesses))
    print('Play again? (Y/N)')
    ans = input()
    if ans == 'Y':
        continue
    elif ans == 'N':
        break
