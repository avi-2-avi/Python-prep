#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s[:-2]
    if 'AM' in s:
        if '12' in s:
            return('00' + time[2:])
        return(time)
    elif 'PM':
        if '12' in s:
            return(str(time))
        hour, rest = time.split(':', 1)
        hour = int(hour) + 12
        return(str(hour) + ":" + rest)
        
                 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
