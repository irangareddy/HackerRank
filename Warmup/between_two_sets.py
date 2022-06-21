#!/bin/python3

# HackerRank Enable
# import os

def getTotalX(a, b):
    """ Get Total Count"""
    min = a[-1:]
    max = b[:1]
    considered_numbers = []
    for num in a:
        values = [x for x in range(min[0], max[0]+1) if num%x == 0 or x%num == 0]
        considered_numbers += values
    refined_numbers = [x for x in considered_numbers if considered_numbers.count(x) == len(a)]
    factors = []
    for num in b:
        values = [x for x in set(refined_numbers) if num%x == 0]
        factors += values

    refined_factors = [x for x in factors if factors.count(x) == len(b)]
    
    return len(set(refined_factors))

        
if __name__ == '__main__':
    # HackerRank Enable
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # HackerRank Disable
    print(total)

    # HackerRank Enable
    # fptr.write(str(total) + '\n')
    # fptr.close()

