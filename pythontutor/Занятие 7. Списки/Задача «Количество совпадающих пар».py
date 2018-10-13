a = input().split()
s = 0
for i in range(len(a)):
    s += a[i+1::].count(a[i])
print(s)
