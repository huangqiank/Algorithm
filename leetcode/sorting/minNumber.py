##剑指 Offer 45. 把数组排成最小的数
#输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#示例 1:
#输入: [10,2]
#输出: "102"
#示例 2:
#输入: [3,30,34,5,9]
#输出: "3033459"

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        return "".join(self.merge(nums))
    def merge(self,nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = self.merge(nums[:mid])
        right = self.merge(nums[mid:])
        return self.merge_help(left,right)

    def merge_help(self,left,right):
        res=[]
        i=0
        j=0
        while i <len(left) and j < len(right):
            if int(left[i] + right[j]) < int(right[j] + left[i]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        return res


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        n = len(nums)
        self.quick_sort(0, n - 1, nums)
        return "".join(nums)

    def quick_sort(self, left, right, nums):
        if left >= right:
            return
        index = self.help(left, right, nums)
        self.quick_sort(left, index - 1, nums)
        self.quick_sort(index + 1, right, nums)

    def help(self, left, right, nums):
        i = left - 1
        tmp = left
        while tmp < right:
            if int(nums[tmp] + nums[right]) < int(nums[right] + nums[tmp]):
                i += 1
                nums[tmp], nums[i] = nums[i], nums[tmp]
            tmp += 1
        i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i

