# -*- coding: utf-8 -*-


def mode(n, arr):
    cnts = {}
    for i in arr:
        if i in cnts:
            cnts[i] += 1
        else:
            cnts[i] = 1
    modes = []
    mode_cnt = max(cnts.values())
    for k, v in cnts.items():
        if v == mode_cnt:
            modes.append(k)
    modes.sort()
    mode = modes[0]
    return mode
    
def mean(n, arr):
    s = sum(arr)
    m = s / len(arr)
    return m

def median(n, arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ind = (len(arr) - 1) / 2
        m = arr[ind]
    else:
        ind_2 = len(arr) // 2
        ind_1 = ind_2 - 1
        m = (arr[ind_1] + arr[ind_2]) / 2
    return m



n = int(input())
arr = [int(i) for i in input().split(' ')]
print(mean(n, arr))
print(median(n, arr))
print(mode(n, arr))




        

