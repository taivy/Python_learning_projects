# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = s.count('a')
    cnt *= n // len(s)
    left = n % len(s)
    cnt += s[:left].count('a')
    print(cnt)
    return cnt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
