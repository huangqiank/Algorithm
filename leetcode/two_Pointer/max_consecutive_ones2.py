##Given a binary array,
##find the maximum number of consecutive 1s in this array
##if you can flip at most one 0.
##Example 1:
##Input: [1,0,1,1,0]
##Output: 4
##Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
##After flipping, the maximum number of consecutive 1s is 4.
##Note:
##The input array will only contain 0 and 1.
##The length of input array is a positive integer and will not exceed 10,000
##Follow up:
##What if the input numbers come in one by one as an infinite stream?
# In other words, you can't store all numbers coming from the stream as it's too large to hold in memory.
# Could you solve it efficiently?

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if not nums or len(nums) == 0:
            return 0
        num_dict = {0: 0, 1: 0}
        left = 0
        right = 0
        max_length =0
        if len(nums) ==1:
            return 1
        ##区别while 和for while不用加1 for 要加一
        while right < len(nums):
            num_dict[nums[right]] += 1
            right += 1
            while num_dict[0] > 1:
                num_dict[nums[left]] -= 1
                left += 1
            max_length = max(max_length,right-left)
        return max_length

nums = [1,0,1,1,0,1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))