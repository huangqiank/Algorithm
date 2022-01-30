#238. 除自身以外数组的乘积
#给你一个长度为 n 的整数数组 nums，其中 n > 1，
# 返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#示例:
#输入: [1,2,3,4]
#输出: [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums):
        l=[]
        r=[]
        res=[]
        n = len(nums)
        tmp=1
        for i in range(n):
            l.append(tmp)
            tmp = tmp*nums[i]
        tmp = 1
        for i in range(n-1,-1,-1):
            r.append(tmp)
            tmp=tmp*nums[i]
        r.reverse()
        for i in range(n):
            res.append(l[i]*r[i])
        return res

class Solution:
    def productExceptSelf(self, nums):
        l = []
        r = []
        n = len(nums)
        res = [0 for i in range(n)]
        tmp =1
        for i range(n):
            l.append(tmp)
            tmp *= nums[i]
        tmp=1
        for j in range(n-1,-1,0):
            r.append(tmp)
            tmp*= nums[j]
        r.reverse()
        for i in range(n):
            res[i] = l[i] * r[i]
        return res