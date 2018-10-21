
dict_1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dict_2 = {v:k for k,v in dict_1.items()}

def check(n, base):
    for i in str(n):
        if i in dict_1:
            i = dict_1[i]
        if int(i) >= base:
            return False
    return True

def convert_from(n, base):
    n = str(n)
    result = 0
    pow = len(n) - 1
    dict_lookup = base >= 10
    for i in n:
        if dict_lookup:
            if i in dict_1:
                i = dict_1[i]
        result += int(i) * int(base)**pow
        pow -= 1
    return result

def convert_to(n, base):
    result = []
    n = int(n)
    while n >= base:
        new_sym = n % base
        if new_sym >= 10:
            new_sym = dict_2[new_sym]
        result.append(str(new_sym))
        n //= base
    result.append(str(n))
    result.reverse()
    return ''.join(result)


print('Supported bases: 2 to 16')
print('Enter number to convert, the base the number is in, and the base to convert the number to '
      '(comma separated, without whitespaces)')
nums = input().split(',')
num, base_from, base_to = nums
base_from = int(base_from)
base_to = int(base_to)

if check(num, base_from) == False:
    print('Incorrent number')

if base_from != 10:
    num = convert_from(num, base_from)
    print(num)

print(convert_to(num, base_to))