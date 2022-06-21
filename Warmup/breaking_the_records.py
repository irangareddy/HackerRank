#!/bin/python3

# HackerRank Enable
# import os

def breakingRecords(scores):
    highest_score = int()
    least_score = int()
    best_record = []
    worst_record = []
    for i in enumerate(scores):
        if i[0] == 0:
            highest_score = i[1]
            least_score = i[1]
        if highest_score < i[1]:
            # score update
            highest_score = i[1]
            # add best position
            best_record.append(i[0])
        elif least_score > i[1]:
            # score update
            least_score = i[1]
            # add least position
            worst_record.append(i[0])
            
    return len(best_record),len(worst_record)

if __name__ == '__main__':
    # HackerRank Enable
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    # HackerRank Disable
    print(result)

    # HackerRank Enable
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
