# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = -1
    i = 0
    while i < len(c):
        print(i)
        if i != len(c) - 2 and i != len(c) - 1:
            if c[i+2] == 0:
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    print(cnt)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
