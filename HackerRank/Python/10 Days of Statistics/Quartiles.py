# -*- coding: utf-8 -*-

def median(n, arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ind = (len(arr) - 1) // 2
        m = arr[ind]
    else:
        ind_2 = len(arr) // 2
        ind_1 = ind_2 - 1
        m = (arr[ind_1] + arr[ind_2]) // 2
    return m

def quartiles(n, arr):
    q2 = median(n, arr)
    if len(arr) % 2 == 1:
        ind = (len(arr) - 1) // 2
        l = arr[:ind]
        r = arr[ind+1:]
    else:
        ind_2 = len(arr) // 2
        ind_1 = ind_2 - 1
        l = arr[:ind_1] + [q2]
        r = arr[ind_2 + 1:] + [q2]
    q1 = median(len(l), l)
    q3 = median(len(r), r)
    
    return q1, q2, q3
        
    

n = int(input())
arr = [int(i) for i in input().split(' ')]
q1, q2, q3 = quartiles(n, arr)
print(q1, q2, q3, sep='\n')

