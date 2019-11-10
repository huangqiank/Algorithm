##Implement pow(x, n),
##which calculates x raised to the power n (xn
def myPow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2:
        return x * myPow(x, n - 1)
    return myPow(x * x, n / 2)

print(myPow(3,-2))