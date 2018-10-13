a = input()
n = 0
s = 0
string = ''
for i in range(len(a)):
    if a[i] == a[n]:
        s += 1
    else:
        if s != 1:
            string += str(s) + a[n]
        else:
            string += a[n]
        s = 1
        n = i
    if i == len(a) - 1:
        if s != 1:
            string += str(s) + a[n]
        else:
            string += a[n]
print(string)