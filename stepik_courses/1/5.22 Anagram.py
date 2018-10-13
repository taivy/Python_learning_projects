a = input().lower()
b = input().lower()
if b == '':
    print(False)
else:
    d = {}
    anagram = True
    for i in a:
        d[i] = a.count(i)
    for i in b:
        if b.count(i) != d.get(i):
            anagram = False
    print(anagram)




data=sorted(input().lower())
result=sorted(input().lower())
print(data==result)