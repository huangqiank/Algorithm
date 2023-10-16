##Given an array of citations (each citation is a non-negative integer)of a researcher,
# write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each."
# Example:
##Input: citations = [3,0,6,1,5]
##Output: 3
##Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
##received 3, 0, 6, 1, 5 citations respectively.
##Since the researcher has 3 papers with at least 3 citations each and the remaining
##two with no more than 3 citations each, her h-index is 3.
def hIndex(citations):
    ##倒着排序然后找到第一个小于index的
    if not citations:
        return 0
    citations = sorted(citations, key=lambda citation: citation, reverse=True)
    l = 0
    r = len(citations) - 1
    while l + 1 < r:
        mid = int((l + r) / 2)
        if citations[mid] == mid + 1:
            l = mid
        if citations[mid] < mid + 1:
            r = mid
        if citations[mid] > mid + 1:
            l = mid
    if citations[r] >= r + 1:
        return r+1
    if citations[l] >= l + 1:
        return l+1
    return 0
a = [0]
print(hIndex(a))
a= "1234"
print([int(i) for i in a])