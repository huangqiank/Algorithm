##Given an array of n integers nums and a target,
##find the number of index triplets i, j,
##k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
##Example:
##Input: nums = [-2,0,1,3], and target = 2
##Output: 2
##Explanation: Because there are two triplets which sums are less than 2:
##             [-2,0,1]
##             [-2,0,3]
##Follow up: Could you solve it in O(n2) runtime?

def threeSumSmaller(nums, target):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[i] + nums[r] == target:
                tmp = nums[r]
                while l < r and nums[r] == tmp:
                    r -= 1
            if nums[l] + nums[i] + nums[r] < target:
                count = count + r - l
                l += 1
            else:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
    return count


nums = [-2,0,1,3]

target = 2
print(threeSumSmaller(nums, target))
