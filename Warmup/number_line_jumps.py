#!/bin/python3

# HackerRank Enable
# import os

def kangaroo(x1, v1, x2, v2):
    if (x2-x1)*(v2-v1) < 0:
        if (x2-x1)%(v2-v1) == 0:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    # HackerRank Enable
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    
    # HackerRank Disable
    print(result)
    # HackerRank Enable
    # fptr.write(result + '\n')
    # fptr.close()
