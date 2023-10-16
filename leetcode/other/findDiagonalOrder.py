##1424. Diagonal Traverse II
#Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
#Example 1:
#Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,4,2,7,5,3,8,6,9]


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        rec = defaultdict(list)
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(len(nums[i])):
                rec[i + j].append(nums[i][j])
        for key in sorted(rec.keys()):
            res.extend(rec[key][::-1])
        return res