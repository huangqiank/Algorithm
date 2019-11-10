# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Example 1:
# Input: 4
# Output: 2
# Example 2:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
# class Solution:
# def mySqrt(self, x: int) -> int:
###注意最后大于的时候减1
class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        i = 1  ###1
        j = int(x / 2) + 1  ###2
        while i + 1 < j:
            center = int((i + j) / 2)  ###1.5
            if center ** 2 == x:
                return int(center)
            elif center ** 2 > x:
                j = center
            else:
                i = center
        if i ** 2 >= x:
            return i - 1
        if j ** 2 >= x:
            return j - 1


def mysqrts(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    i = 1
    j = int(x / 2) + 1
    while i + 1 < j:
        center = int((i + j) / 2)
        if center ** 2 == x:
            return int(center)
        elif center ** 2 > x:
            j = center
        else:
            i = center
    if i ** 2 == x:
        return i
    if j ** 2 == x:
        return j
    if i ** 2 > x:
        return i - 1
    if j ** 2 > x:
        return j - 1
print(mysqrts(5))