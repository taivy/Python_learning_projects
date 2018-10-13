
def bin_to_decimal(n):
    base = 2
    power = len(str(n)) - 1
    result = 0
    for num in str(n):
        result += int(num) * base**power
        power -= 1
    return result

def decimal_to_bin(n):
    bin_arr = []
    while n >= 1:
        bin_num = n % 2
        bin_arr.append(str(bin_num))
        n //= 2
    bin_arr.reverse()
    result = ''.join(bin_arr)
    return result

a = decimal_to_bin(25)
print(a)

a = decimal_to_bin(11001)
print(b)

