tmpOut = ''
with open('dataset_3363_2.txt') as inf:
    s = inf.readline().strip()
    char = ''
    count = 0
    for i in s:
        if i.isdigit():
            count += i
        elif i.isalpha():
            tmpOut += char * int(count)
            char = i
            count = ''
    tmpOut += char * int(count)
print(tmpOut)
with open('dataset_3363_2.txt', 'w') as ouf:
    ouf.write(tmpOut)
