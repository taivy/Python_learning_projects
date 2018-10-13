def modify_list(l):
    for n in range(len(l) - 1, -1, -1):
        if l[n] % 2 == 1:
            del l[n]
    b = [a // 2 for a in l]
    for i in range(len(l)):
        del l[0]
    for i in range(len(b)):
        l += [b[i]]
