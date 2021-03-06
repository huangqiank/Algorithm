##Given a string s , find the length of the longest substring t  
##that contains at most 2 distinct characters.
##Example 1:
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n
        max_length = 0
        left = 0
        right = 0
        s_dict = {}
        ##记录字符出现的最后一个位置
        while right < n:
            if len(s_dict) < 3:
                s_dict[s[right]] = right
                right += 1
            if len(s_dict) == 3:
                del_index = min(s_dict.values())
                s_dict.pop(s[del_index])
                left = del_index +1
            ##在不足三个的情况下也会更新max_length
            max_length = max(right - left, max_length)
        return max_length


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eeeddc"))



def length_longest_substring_two_distinct(nums):
    left = 0
    right = 0
    max_length = 0
    nums_dict = {}
    n = len(nums)
    if n < 3:
        return n
    while right < n:
        if nums[right] not in nums_dict:
            nums_dict[nums[right]] = 1
        else:
            nums_dict[nums[right]] += 1
        right += 1
        while len(nums_dict) >= 3:
            nums_dict[nums[left]] -= 1
            if nums_dict[nums[left]] == 0 :
                del nums_dict[nums[left]]
            left += 1
        max_length = max(max_length,right-left)
    return max_length

