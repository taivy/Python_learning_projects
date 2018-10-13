a = int(input())
b = input()
descriptor = ''.join([chr(x) for x in range(128512, 128592)])
d = {}
for i in range(len(descriptor)):
    d[descriptor[i]] = i
inv_d = {v: k for k, v in d.items()}
str = ''
for i in b:
    j = (d[i] + a) % 80
    c = inv_d[j]
    str += c
print('Result: "' + str + '"')