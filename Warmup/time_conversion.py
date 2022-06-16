#!/bin/python3
import os

def timeConversion(s):
    """ Time Conversion Code """
    
    try:
        h,m,sec = map(int, s[:-2].split(':'))
        meridiem = s[-2:]
        h = h % 12 + (meridiem.upper() == 'PM') * 12
        return ('%02d:%02d:%02d') % (h, m, sec)
    except ValueError:
        return 'EXPECTED INPUT FORMAT hh:mm:ssAM or hh:mm:ssPM'

def test_execution():
    """ Basic Test Cases """

    assert timeConversion(s='12:01:01PM') == '12:01:01'
    assert timeConversion(s='12:01:01AM') == '00:01:01'
    assert timeConversion(s='217$%&') == 'EXPECTED INPUT FORMAT hh:mm:ssAM or hh:mm:ssPM'
        
if __name__ == '__main__':
    # HackerRank Enable
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)

    # HackerRank Disable
    print(result)

    # HackerRank Enable
    # fptr.write(result + '\n')
    # fptr.close()

    test_execution()