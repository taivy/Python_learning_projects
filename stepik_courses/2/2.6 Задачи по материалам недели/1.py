a = 1
s = 0
ss = 0
while a == 1:
    i = int(input())
    s += i
    si = i*i
    ss += si
    if s == 0:
        print(ss)
        break