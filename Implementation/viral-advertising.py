def viral_advertising(n):
    """viral advertising"""
    assert 1 <= n <= 50
    shared = 5
    cumulative = 0
    for _ in range(1, n + 1):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


assert viral_advertising(5) == 24
assert viral_advertising(3) == 9
assert viral_advertising(12) == 424
