import bisect


def p():
    return bisect.bisect_left([1,2,2,4,5,5],3)
print(p())