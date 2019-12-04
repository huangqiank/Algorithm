def minSubArrayLen(s, nums):
    l = 0
    r = 0
    res = float("inf")
    for j in range(len(nums)):
        r += nums[j]
        while r >= s:
            res = min(res, j - l + 1)
            r -= nums[l]
            l += 1
    if res == float("inf"):
        return 0
    return res


def lengthOfLongestSubstring(s):
    if not s or len(s) == 0:
        return 0
    word = set()
    l = 0
    max_length = -float("inf")
    for r in range(len(s)):
        while s[r] in word:
            word.discard(s[l])
            l += 1
        word.add(s[r])
        max_length = max(max_length, len(word))
    return max_length


print(lengthOfLongestSubstring("a"))


def checkInclusion(s1, s2):
    if not s1 and not s2:
        return True
    if len(s1) == 0 and len(s2) == 0:
        return True
    if not s1 or not s2 or len(s1) == 0 or len(s2) == 0:
        return False
    s1_word_dict = {}
    for i in range(len(s1)):
        s1_word_dict[s1[i]] = s1_word_dict.get(s1[i], 0) + 1
    n = len(s1)
    l = 0
    s2_word_dict = {}
    for r in range(len(s2)):
        s2_word_dict[s2[r]] = s2_word_dict.get(s2[r], 0) + 1
        while r - l + 1 > n:
            s2_word_dict[s2[l]] = s2_word_dict[s2[l]] - 1
            if s2_word_dict[s2[l]] == 0:
                del s2_word_dict[s2[l]]
            l += 1
        if r - l + 1 == n and s2_word_dict == s1_word_dict:
            return True
    return False


def longest_turbulen_subarray(A):
    if not A or len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    nums = []
    dp = [0 for i in range(len(A))]
    if A[0] == A[1]:
        dp[0] = 0
    else:
        dp[0] = 1
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            nums.append(1)
        if A[i] < A[i - 1]:
            nums.append(-1)
        if A[i] == A[i - 1]:
            nums.append(0)
    for i in range(1, len(nums)):
        if nums[i] == 0:
            dp[i] = 0
        elif nums[i] + nums[i - 1] == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    return max(dp) + 1


print(longest_turbulen_subarray([9, 4, 2, 10, 7, 8, 8, 1, 9]))
