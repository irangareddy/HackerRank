def beautiful_days(start, stop, divider):
    """beautiful days"""
    days = []
    for i in range(start, stop + 1):
        day = (i - reversed_number(i)) / divider
        if day.is_integer():
            days.append(day)
    return len(days)


def reversed_number(num: int):
    """reversed number"""
    return int(str(num)[::-1])


assert beautiful_days(20, 23, 6) == 2
assert beautiful_days(13, 45, 3) == 33
