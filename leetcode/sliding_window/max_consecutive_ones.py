##Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
##Return the length of the longest (contiguous) subarray that contains only 1s. 
##Example 1:
##Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
##Output: 6
##Explanation:
##[1,1,1,0,0,1,1,1,1,1,1]
##Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
##Example 2:
##Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
##Output: 10
##Explanation:
##[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
##Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
##Note:
##1 <= A.length <= 20000
##0 <= K <= A.length
##A[i] is 0 or 1 
def longestOnes(A, k):
    if not A or len(A) == 0 or k < 0:
        return 0
    if len(A) == 1:
        if A[1] == 1:
            return 1
        return
    num_dict = {0: 0, 1: 0}
    l = 0
    length = 0
    for r in range(len(A)):
        num_dict[A[r]] = num_dict.get(A[r], 0) + 1
        while num_dict[0] > k:
            num_dict[A[l]] = num_dict[A[l]] - 1
            l += 1
        length = max(length, r - l + 1)
    return length


print(longestOnes( [1,0,1,1,0,1], 1))


def longestOnes2(A, K):
    res = 0
    num_dict = {0: 0, 1: 1}
    l = 0
    if not A or len(A) == 0:
        return 0
    if len(A) == 1:
        if A[1] == 1:
            return 1
        return 0
    for r in range(len(A)):
        num_dict[A[r]] = num_dict.get(A[r], 0) + 1
        while num_dict[0] > K:
            num_dict[A[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


print(longestOnes2([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
