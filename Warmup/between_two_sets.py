#!/bin/python3



def getTotalX(a, b):
    # Write your code here
    min = a[-1:]
    max = b[:1]
    values = []
    excludes = []
    
    for i in range(min[0], max[0]):
        for num in a:
            if num > i:
                if num%i == 0:
                    values.append(i)
                elif values.count(i) > 0:
                    values.remove(i)
            elif i%num == 0:
                values.append(i)

    values = list(set(values))
    for i in values:
        for num in b:
            if num%i == 0:
                print('a',num,i)
                excludes.append(i)
            elif excludes.count(i) > 0:
                print('r',num,i)
                set(excludes).remove(i)
    return excludes

    

print(getTotalX([2,4],[16,32,96]))