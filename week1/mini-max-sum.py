#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr = sorted(arr) 
    min_n = arr[0]
    max_n = arr[len(arr) - 1]
    print(sum(arr)-max_n, sum(arr)-min_n)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
