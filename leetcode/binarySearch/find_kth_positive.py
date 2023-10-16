# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
# 请你找到这个数组里第 k 个缺失的正整数。
# 示例 1：
# 输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
# 示例 2：
# 输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
class Solution:
    def findKthPositive(self, arr, k):
        count, index = 0, 0
        tmp = 1
        n = len(arr)
        while count < k and index < n:
            if arr[index] == tmp:
                tmp += 1
                index += 1
            elif arr[index] > tmp:
                count += 1
                tmp += 1
        if count == k:
            return tmp - 1
        if index == n:
            tmp += k - count - 1
            return tmp


s = Solution()
arr = [1, 2, 3, 4]
k = 2
print(s.findKthPositive(arr, k))
arr = [2, 3, 4, 7, 11]
k = 5
print(s.findKthPositive(arr, k))


## ninary search