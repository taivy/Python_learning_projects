n = int(input())
a = input()
alph = ' abcdefghijklmnopqrstuvwxyz'
d = {}
for i in range(len(alph)):
    d[alph[i]] = i
d2 = {}
for i in d.keys():
    key2 = d[i]
    d2[key2] = i
input = 'Result: "'
for i in a:
    j = (d[i] + n) % 27
    input += d2[j]
input += '"'
print(input)