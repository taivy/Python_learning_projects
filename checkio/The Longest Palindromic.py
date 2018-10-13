def longest_palindromic(text):
    l = [[i] for i in text]
    li = 0
    for i in range(1, len(text)):
        li += 1
        n = 1
        if i < len(text) - i:
            maxi = i
        else:
            maxi = len(text) - 1 - i
        while (n <= maxi) or (i == 1 and n <= 1):
            if text[i-n] == text[i+n]:
                l[li].insert(0, text[i-n])
                l[li].append(text[i-n])
                n += 1
            else:
                break
    if len(text) % 2 == 0:
        l += [[]]
        li += 1
        i1 = (len(text) // 2) - 1
        i2 = i1 + 1
        mini = 0
        maxi = len(text) - 1
        while i1 >= mini and i2 <= maxi:
            if text[i1] == text[i2]:
                l[li].insert(0, text[i1])
                l[li].append(text[i1])
                i1 -= 1
                i2 += 1
            else:
                break
    m = max([len(i) for i in l])
    for i in l:
        if len(i) == m:
            print(''.join(i))
            return ''.join(i)
