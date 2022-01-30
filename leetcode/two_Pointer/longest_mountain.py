
##845. 数组中的最长山脉
# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
# 如果不含有 “山脉” 则返回 0。
# 示例 1：
# 输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。



class Solution:
    def longestMountain(self, arr):
        peaks=[]
        n = len(arr)
        for i in range(1,n-1):
            if arr[i]> arr[i-1] and arr[i]>arr[i+1]:
                peaks.append(i)
        max_l=0
        for peak in peaks:
            tmp=1
            i,j=peak,peak
            while i>0 and arr[i-1] <arr[i]:
                tmp+=1
                i-=1
            while j< n-1 and arr[j]>arr[j+1]:
                tmp+=1
                j+=1
            max_l =max(max_l,tmp)
        return max_l

s=Solution()
print(s.longestMountain([1,4,7,3,2]))