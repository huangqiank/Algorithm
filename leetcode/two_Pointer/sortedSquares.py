##977. 有序数组的平方
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 示例 1：
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums):
        i = 0
        n = len(nums)
        negative=-1
        for i in range(n):
            if nums[i]<0:
                negative =i
        positive = negative+1
        res=[]
        while negative >=0 or positive<=n-1:
            if negative <0:
                res.append(nums[positive]*nums[positive])
                positive+=1
            elif positive>=n:
                res.append(nums[negative]*nums[negative])
                negative-=1
            elif nums[positive]*nums[positive] <= nums[negative]*nums[negative]:
                res.append(nums[positive]*nums[positive])
                positive+=1
            else:
                res.append(nums[negative]*nums[negative])
                negative-=1
        return res



s=Solution()
print(s.sortedSquares([-1]))
a = {"a":1,"b":2}
b = {"b":2,"a":1}
print(sorted(a.keys()),sorted(b.keys()))
print([] +[2])