# Given an array with n objects colored red,
# white or blue, sort them in-place 
# so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers
# 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums):
        if not nums:
            return nums
        p=0
        q = len(nums)-1
        self.quick_sort(nums,p,q)
    def quick_sort(self,nums,p,q):
        if p<q:
            d = self.quick_sort_help(nums,p,q)
            self.quick_sort(nums,d+1,q)
            self.quick_sort(nums,p,d-1)
    def quick_sort_help(self,nums,p,q):
        j = p-1
        for i in range(p,q):
            if nums[i] < nums[q]:
                j+=1
                nums[i],nums[j] = nums[j],nums[i]
        j+=1
        nums[j],nums[q] = nums[q],nums[j]
        return j


a= "abcdef"
print(a[:3])
print(a[:3] + "e" + a[3:])
print(a[6:])
print(a[0])