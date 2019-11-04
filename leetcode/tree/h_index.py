# Given an array of citations sorted in ascending order
# (each citation is a non-negative integer) of a researcher,
# write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each."

a = [1, 1, 3]


def hIndex(citations):
    if not citations:
        return 0
    citations = sorted(citations, key=lambda key: key, reverse=True)
    for i in range(0, len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)


def hIndex2(citations):
    if not citations:
        return 0
    left = 0
    right = len(citations) - 1
    citations = sorted(citations, key=lambda key: key, reverse=True)
    while left + 1 < right:
        mid = int((left + right) / 2)
        if citations[mid] < mid + 1:
            right = mid
        elif citations[mid] == mid + 1:
            left = mid
        elif citations[mid] > mid + 1:
            left = mid
    if citations[right] >= right + 1:
        return right + 1
    if citations[left] >= left + 1:
        return left + 1
    return 0


print(hIndex(a))
