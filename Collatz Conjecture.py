
def collatz(n):
    if n < 2:
        return
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            steps += 1
        else:
            n = n*3 + 1
            steps += 1
    return steps

a = int(input())
b = collatz(a)
print(b)








