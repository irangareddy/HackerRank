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
    # Write your code here
    h,m,sec = map(int, s[:-2].split(':'))
    meridiem = s[-2:]
    h = h % 12 + (meridiem.upper() == 'PM') * 12
    return ('%02d:%02d:%02d') % (h, m, sec)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
