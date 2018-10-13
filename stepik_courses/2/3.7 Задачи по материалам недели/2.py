a = input()
b = input()
d1 = {}
d2 = {}
for i in range(len(a)):
    d1[a[i]] = b[i]
    d2[b[i]] = a[i]
c = input()
str1 = ''
for i in c:
    str1 += d1[i]
d = input()
str2 = ''
for i in d:
    str2 += d2[i]
print(str1)
print(str2)
