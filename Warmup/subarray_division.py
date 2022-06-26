#!/bin/python3

def birthday(s, d, m):
    print(s[0:2])
    result = [x for i in range(len(s)) if s[i]==2]
    print(result)
    return sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])

    

result = birthday(s=[1,2,3,4,5],d=3,m=3)
print(result)