a = input().split()
a = list(map(int, a))
for i in range(len(a) - 1):
    if a[i] > 0 and a[i+1] > 0 or a[i] < 0 and a[i+1] < 0:
        print(a[i], a[i+1])
        break