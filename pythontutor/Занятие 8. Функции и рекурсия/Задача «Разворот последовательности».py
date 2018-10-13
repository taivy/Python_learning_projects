def reverse():
    a = input()
    if a == '0':
        print(a)
        return a
    else:
        reverse()
        print(a)

reverse()