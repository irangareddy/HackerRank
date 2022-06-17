#!/bin/python3

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """ Code for Apples and Oranges """
    apples_landing_poisition = []
    for pos in apples:
        apples_landing_poisition.append(a+pos)
    oranges_landing_poisition = []
    for pos in oranges:
        oranges_landing_poisition.append(b+pos)
        
    print(get_count(start=s,end=t,data=apples_landing_poisition))
    print(get_count(start=s,end=t,data=oranges_landing_poisition))
        
    
def get_count(start: int, end: int, data: list):
    """ get total range matches of the element in array"""
    count = 0
    for value in enumerate(data):
        if start <= value[1] and end >= value[1]:
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
