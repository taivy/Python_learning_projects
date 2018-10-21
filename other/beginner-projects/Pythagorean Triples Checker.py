
while True:
    print("Enter 'quit' to exit, anything else or nothing to continue")
    if_exit = input()
    if if_exit == 'exit':
        break

    print(r'Enter three integers (comma separated, without whitespaces):')
    num_input = input()
    nums_str = num_input.split(',')

    if len(nums_str) != 3:
        print('Impermissible number of integers')
        continue
    else:
        ints = map(int, nums_str)
        x, y, z = ints
        if x**2 + y**2 == z**2:
            print('Pythagorean Triple')
        else:
            print('Not Pythagorean Triple')
