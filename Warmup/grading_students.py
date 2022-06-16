#!/bin/python3

# HackerRank Enable
# import os

from socket import gaierror


def gradingStudents(grades):
    """ grading students code """
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            diff = grade%5
            if (diff >= 3):
                result.append(grade+ (5-diff))
            else:
                result.append(grade)
    return result

def test_execution():
    assert gradingStudents(grades=[73,67,50,22]) == [75,67,50,22]
    assert gradingStudents(grades=[13,72,38]) == [13,72,40]

if __name__ == '__main__':
    # HackerRank Enable
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    # HackerRank Disable
    print(result)

    # HackerRank Disable
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
    test_execution()
