##Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
##Example:
##Input: 3
##Output: 5
##Explanation:
##Given n = 3, there are a total of 5 unique BST's:
##   1         3     3      2      1
##    \       /     /      / \      \
##     3     2     1      1   3      2
##    /     /       \                 \
##   2     1         2                 3
##G(0) = 1
##G(1) = 1
##G(n) = sum(F(i,n))
##F(i,n) = G(i-1)*G(n-i)
##G(n) = sum(G(i-1) *G(n-i)）


def numTrees(n):
    res = []
    if n == 0 or n == 1:
        return 1
    res = [0 for i in range(n+1)]
    res[0] = 1
    res[1] = 1
    for i in range(2, n+1, 1):
        for j in range(i+1):
            res[i] += res[j - 1] * res[i - j]
    return res

print(numTrees(3))