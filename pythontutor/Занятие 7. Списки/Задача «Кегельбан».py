n, k = map(int, input().split())
out = ['I' for i in range(n)]
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        out[j] = '.'
print(''.join(out))