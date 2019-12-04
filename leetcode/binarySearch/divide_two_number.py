# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2


def divide_two_number(a, b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        flag = 1
    else:
        flag = -1
    a = abs(a)
    b = abs(b)
    i = 0
    max_num = 2**31 -1
    min_num = -2**31
    while a << i <= b:
        i += 1
    ## a*2^i <=b
    res = 0
    for j in reversed(range(i)):
        if b >= a << j:
            b -= a << j
            res += 1 << j
    if flag == 1:
        return min(res,max_num)
    else:
        return max(-res,min_num)


print(divide_two_number(2, 10))



def divide(dividend, divisor):
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        k = 1
    else:
        k = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    i = sub_minus(dividend, divisor)
    if (k == 1):
        return i
    else:
        return 0 - i

def sub_minus(dividend, divisor):
    i = 0
    while dividend >= divisor:
        i += 1
        dividend -= divisor
    return i





def divided_integer(q, p):
    a = abs(p)
    b = abs(q)
    if a == 0:
        print(0)
    i = 0
    while a << i <= b:
        i += 1
    res = 0
    for t in reversed(range(i)):
        if b >= a << t:
            b -= a << t
            res += 1 << t
    max_num = 2 ** 31 - 1
    min_num = -2 ** 31

    if (p > 0 and q > 0) or (p < 0 and q < 0):
        return min(res, max_num)
    return max(-res, min_num)


