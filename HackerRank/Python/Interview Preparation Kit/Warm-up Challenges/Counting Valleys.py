# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    cnt = 0
    for step in s:
        if step == "D":
            sea_level -= 1
        elif step == "U":
            sea_level += 1
            if sea_level == 0:
                cnt += 1
    return cnt
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
