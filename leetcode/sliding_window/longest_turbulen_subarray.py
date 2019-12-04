##A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
##For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
##OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
##That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
##Return the length of a maximum size turbulent subarray of A.
##Example 1:
##Input: [9,4,2,10,7,8,8,1,9]
##Output: 5
##Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
##Example 2:
##Input: [4,8,12,16]
##Output: 2
##Example 3:
##Input: [100]
##Output: 1
##Note:
##1 <= A.length <= 40000
##0 <= A[i] <= 10^9

def maxTurbulenceSize(A):
    i = 0
    length = 0
    if not A:
        return 0
    if len(A) <= 1:
        return len(A)
    while i < len(A):
        j = i
        res = []
        while j < len(A):
            if len(res) == 0:
                new_flag = 0
                old_flag = 0
                res.append(A[j])
                j += 1
                continue
            if len(res) == 1:
                new_flag = check(res[-1], A[j])
                if new_flag != 0:
                    res.append(A[j])
                    j += 1
                    old_flag = new_flag
                    continue
                else:
                    length = 1
                    break
            if len(res) >= 2:
                print(res)
                new_flag = check(res[-1], A[j])
                if new_flag * old_flag < 0:
                    res.append(A[j])
                    j += 1
                    old_flag = new_flag
                    continue
                else:
                    length = max(length, len(res))
                    break
        if new_flag == 0:
            i = j
        else:
            i = j - 1
        length = max(length, len(res))
    length = max(length, len(res))
    return length


def check(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    return -1


print(maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24]))


def maxTurbulenceSize(A):
    """
        1. dp问题: 这里我们不应该关注数值本身, 而是应该关注变化的趋势.
            所以, 对于A = [9,4,2,10,7,8,8,1,9], 变更为: [-1, -1, 1, -1, 1, 0, -1, 1]
            A[i+1]>A[i], 则为1, A[i+1]=A[i], 则为0, 否则为-1
        2. dp[i] = dp[i-1] + 1, 如果nums[i], nums[i-1]为1, -1.(代表上升下降, 或者下降上升)
            dp[i] = 1, 如果nums[i] == nums[i-1](代表上升上升, 或者下降下降)
            dp[i] = 0, 如果nums[i] = 0(代表之前的两数相等)
    """
    if len(A) == 1:
        return 1
    nums = []
    for i in range(1, len(A)):
        v = A[i] - A[i - 1]
        nums.append(1 if v > 0 else 0 if v == 0 else -1)
    dp = [0 for _ in range(len(nums))]
    dp[0] = 0 if nums[0] == 0 else 1
    for i in range(1, len(nums)):
        if nums[i] == 0:
            dp[i] = 0
        elif nums[i] + nums[i - 1] == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

    return max(dp) + 1


print(maxTurbulenceSize([1,1,1,1]))


class Solution:
    def maxTurbulenceSize(self, A) -> int:
        pattern1 = 1
        pattern2 = 1
        ans = 1

        for i in range(1, len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    pattern1 += 1
                else:
                    pattern1 = 1

                if A[i] > A[i - 1]:
                    pattern2 += 1
                else:
                    pattern2 = 1
            else:
                if A[i] > A[i - 1]:
                    pattern1 += 1
                else:
                    pattern1 = 1
                if A[i] < A[i - 1]:
                    pattern2 += 1
                else:
                    pattern2 = 1
            ans = max(ans, pattern1, pattern2)

        return ans




