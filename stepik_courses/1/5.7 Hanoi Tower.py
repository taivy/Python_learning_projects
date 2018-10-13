def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print(start, ' - ', finish)
        move(n - 1, temp, finish)
move(3, 1, 3)