def get_int(start_message, error_message, end_message):
    print(start_message)
    incorrect = True
    while incorrect:
        try:
            a = input()
            a = int(a)
        except ValueError:
            print(error_message)
        else:
            incorrect = False
    print(end_message)
    return int(a)
x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')