a = input().split()
n = input()
ind = []
if n not in a:
    print('None')
for i in range(len(a)):
    if a[i] == n:
        ind += [i]
print(*ind)