##Determine whether an integer is a palindrome.
##An integer is a palindrome when it reads the same backward as forward.

##Example 1:

##Input: 121
##Output: true
##Example 2:

##Input: -121
##Output: false
##Explanation: From left to right,
# it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.
##Example 3:

##Input: 10
##Output: false
##Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
def isPalindrome(x):
    x = str(x)
    y = ""
    for i in range(len(x) - 1, -1, -1):
        y += x[i]
    return x == y


print(isPalindrome(1121))


def isPalindrome2(x):
    if x < 0:
        return False
    m, n = x, 0
    while m:
        n = n * 10 + m % 10
        m = m // 10
    return x==n
print(isPalindrome2(121))