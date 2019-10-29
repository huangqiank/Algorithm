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
    res = 0
    for j in reversed(range(i)):
        if b > 1 << j:
            b -= 1 << j
            res += 1 << j
    if flag == 1:
        return min(res,max_num)
    else:
        return max(-res,min_num)


print(divide_two_number(3, 10))

print(divide_two_number(-3, 10))




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


print(divide(-8, 1))


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


print(divided_integer(10, 3))
print(divided_integer(7, - 3))
print(divided_integer(-3, -1))
print(divided_integer(3, 10))
print(divided_integer(-2147483648, 1))