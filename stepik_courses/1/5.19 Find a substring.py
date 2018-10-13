a = input()
b = input()
l = []
start = 0
end = len(b)
if b not in a:
    print('-1')
else:
    for i in range(len(a)):
        c = a[start:end]
        if c == b:
            l.append(start)
        start += 1
        end += 1
    for i in l:
        print(i, end=' ')