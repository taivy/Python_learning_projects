# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    l = []
    rows = len(arr)
    columns = len(arr[0])
    for col in range(columns-2):
        for row in range(rows-2):
            a = arr[row][col]
            b = arr[row][col+1]
            c = arr[row][col+2]
            d = arr[row+1][col+1]
            e = arr[row+2][col]
            f = arr[row+2][col+1]
            g = arr[row+2][col+2]
            s = a+b+c+d+e+f+g
            l.append(s)
            print(s)
    print(l)
    m = max(l)
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
