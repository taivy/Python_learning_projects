
def factor1(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def factor2(n):
    factors = set()
    for i in range(1, int(n+1 / 2)):
        div_n, mod_n = divmod(n, i)
        if mod_n == 0:
            factors.add(i)
            factors.add(div_n)
    factors = list(factors)
    factors.sort()
    return factors


def check_prime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


print('Enter number:')
num = int(input())

if check_prime(num):
    print('Number is prime')
else:
    print(*factor2(num), sep=', ')

