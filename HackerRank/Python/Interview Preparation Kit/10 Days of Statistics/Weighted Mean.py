# -*- coding: utf-8 -*-

def weighted_mean(n, x, w):
    mult = [x[i]*w[i] for i in range(n)]
    a = sum(mult)
    b = sum(w)
    mean = a / b
    return round(mean, 1)

n = int(input())
x = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]

print(weighted_mean(n, x, w))

