#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    print(arr)
    n = 0
    m = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                n += arr[i][j]
                print('now n is: ', n)
            if i + j == len(arr)-1:
                m += arr[i][j]
                print('now m is: ', m)
    return abs(m - n)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
