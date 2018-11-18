# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_colors = set(ar)
    counts = {}
    for color in unique_colors:
        counts[color] = ar.count(color)
    sum = 0
    for count in counts.values():
        sum += count // 2
    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
