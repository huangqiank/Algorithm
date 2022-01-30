##Given an array of n positive integers and a positive integer s,
## find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead


def minSubArrayLen(s, nums):
    l = 0
    r = 0
    res = float("inf")
    for j in range(len(nums)):
        r += nums[j]
        while r >= s:
            res = min(res, j - l + 1)
            r -= nums[l]
            l += 1
    if res == float("inf"):
        return 0
    return res


##Given a string, find the length of the longest substring without repeating characters.
##Example 1:
##Input: "abcabcbb"
##Output: 3
##Explanation: The answer is "abc", with the length of 3.
##Example 2:
##Input: "bbbbb"
##Output: 1
##Explanation: The answer is "b", with the length of 1.
##Example 3:
##Input: "pwwkew"
##Output: 3
##Explanation: The answer is "wke", with the length of 3.
##Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s):
    if not s or len(s) == 0:
        return 0
    word = set()
    l = 0
    max_length = -float("inf")
    for r in range(len(s)):
        while s[r] in word:
            word.discard(s[l])
            l += 1
        word.add(s[r])
        max_length = max(max_length, len(word))
    return max_length


# print(lengthOfLongestSubstring("a"))

##Given two strings s1 and s2, write a function to return true if s2
##contains the permutation of s1. In other words,
##one of the first string's permutations is the substring of the second string.
##Example 1:
##Input: s1 = "ab" s2 = "eidbaooo"
##Output: True
##Explanation: s2 contains one permutation of s1 ("ba").
##Example 2:
##Input:s1= "ab" s2 = "eidboaoo"
##Output: False
##Note:
##The input strings only contain lower case letters.
##The length of both given strings is in range [1, 10,000].
def checkInclusion(s1, s2):
    if not s1 and not s2:
        return True
    if len(s1) == 0 and len(s2) == 0:
        return True
    if not s1 or not s2 or len(s1) == 0 or len(s2) == 0:
        return False
    s1_word_dict = {}
    for i in range(len(s1)):
        s1_word_dict[s1[i]] = s1_word_dict.get(s1[i], 0) + 1
    n = len(s1)
    l = 0
    s2_word_dict = {}
    for r in range(len(s2)):
        s2_word_dict[s2[r]] = s2_word_dict.get(s2[r], 0) + 1
        while r - l + 1 > n:
            s2_word_dict[s2[l]] = s2_word_dict[s2[l]] - 1
            if s2_word_dict[s2[l]] == 0:
                del s2_word_dict[s2[l]]
            l += 1
        if r - l + 1 == n and s2_word_dict == s1_word_dict:
            return True
    return False


def longest_turbulen_subarray(A):
    if not A or len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    nums = []
    dp = [0 for i in range(len(A))]
    if A[0] == A[1]:
        dp[0] = 0
    else:
        dp[0] = 1
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            nums.append(1)
        if A[i] < A[i - 1]:
            nums.append(-1)
        if A[i] == A[i - 1]:
            nums.append(0)
    for i in range(1, len(nums)):
        if nums[i] == 0:
            dp[i] = 0
        elif nums[i] + nums[i - 1] == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    return max(dp) + 1


class Solution2:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0
        for i in range(1, n + 1, 2):
            begin = 0
            first = sum(arr[begin:begin + i])
            total += first
            while begin + i < n:
                first = first - arr[begin] + arr[begin + i]
                total += first
                begin += 1
        return total


# Given an array nums, write a function to move all 0's to the end of it '
# while maintaining the relative order of the non-zero elements.
##Example:

##Input: [0,1,0,3,12]
##Output: [1,3,12,0,0]
##Note:

##You must do this in-place without making a copy of the array.
# 3Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                j = max(i + 1, j)
                while j < n and nums[j] == 0:
                    j += 1
                if j < n and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums
            i += 1
        return nums


# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]


# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数
# nums = [1, 2, 3]
# target = 4


class Solution:
    def combinationSum4(self, nums, target):
        index = 0
        combination = []
        n = target
        self.nums = nums
        self.res = set()
        self.dfs(index, combination, target, n)
        return len(self.res)

    def dfs(self, index, combination, target, n):
        if index == n or target <= 0:
            if target == 0 and combination not in self.res:
                self.res.add(tuple(combination))
            return
        for num in self.nums:
            self.dfs(index + 1, combination + [num], target - num, n)
            self.dfs(index + 1, combination, target, n)


class Solution2:
    def combinationSum4(self, nums, target):
        # 0.... target-1
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num == 0:
                    dp[i] += 1
                if i - num > 0:
                    dp[i] += dp[i - num]
        return dp[target]


##[a,b,c,d,e,f]
## |a-b|+ |b-c| + |c-d| +|e-f|_...
## ·找 m个最小值， 让左边比他小，右边比他大
##   d e f

##[x0,x1,x2.xi...xj...xn]
##[x0...xj...xi...xn]
# |xi-1-xi|+|xj-xj+1|
##xi-1-xj|+ [xi-xj+i]
##|k-1 k... l-1 l|
## |k-1 l-1 ....k l|
##- |k-1,k| |l-1.l| + |k-1,l-1| + |k,l|

##  - max(k-1,k) - max(l-1,l) + min(k-1,k)+min(l-1,l) + max(k-1,l-1) + max(k,l)- min(k-1,l-1)-min(k,l)_

## a<b<c<d

##  b+d-a-c
## c+d-a-b

## a<b  c<d
##b+d -a-c
## max(a,c)- min(a,c) + max(b,d)- min(b,d)
##
## a>b  c<d
##
## a<b  c>d
## a>b  d>c


class Solution:
    def maxValueAfterReverse(self, nums):
        max_total = 0
        min_total = 0
        return


class Solution1:
    def kLengthApart(self, nums, k):
        n = len(nums)
        i = 0

        while i < n and nums[i] == 0:
            i += 1
        while i < n:
            tmp = 1
            while i + tmp < n and nums[i + tmp] == 0:
                tmp += 1
            if i + tmp < n and nums[i + tmp] == 1 and tmp - 1 < k:
                return False
            i = i + tmp
        return True


##给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
# 其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：
# i - K <= r <= i + K, j - K <= c <= j + K
# (r, c) 在矩阵内。
# 示例 1：
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
###i-k<=r<=i+k   j-k<=c<=j+k
### i-k+1<r<i+k+1    j+1-k<c<j+k+1

## dp[i,j+1] = dp[i,j] - sum row[r][j+k] + row[r][j+k+1]
##dp[i+1,j] = dp[i,j] - sum row[i-k][c] +row[i+k+1][c]

##   i   k
## [        ]

# sum = P[i + K + 1][j + K + 1] - P[i - K][j + K + 1] - P[i + K + 1][j - K] + P[i - K][j - K]

##

class Solution:
    def matrixBlockSum(self, mat, k):
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = sum([col[:j] for col in mat[:i]])
        ans = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = dp[min(i + k + 1, n)][min(j + k + 1, m)] - dp[max(i - k, 0)][min(j + k + 1, m)] - \
                            dp[min(i + k + 1, n)][max(j - k, 0)] + dp[max(i - k, 0)][max(j - k, 0)]
        return ans


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(a) - 1
        pre = "0"
        res = ""
        while i >= 0 and j >= 0:
            if a[i] == "1" and b[j] == "1":
                res = pre + res
                pre = "1"
            if (a[i] == "1" and b[j] == "0") or (a[i] == "0" and b[j] == "1"):
                if pre == "0":
                    res = "1" + res
                else:
                    res = "0" + res
            if a[i] == "0" and b[j] == "0":
                res = pre + res
                pre = "0"
            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == "0":
                res = pre + res
                pre = "0"
            if a[i] == "1":
                if pre == "0":
                    res = "1" + res
                else:
                    res = "0" + res
            i -= 1
        while j >= 0:
            if b[j] == "0":
                res = pre + res
                pre = "0"
            if b[j] == "1":
                if pre == "0":
                    res = "1" + res
                else:
                    res = "0" + res
            j -= 1
        if pre != "0":
            res = pre + res
        return res


# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 示例 1：

# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
## ]  pop 直到出一个数字[
## 数字，字母 或[ push

class Solution9:
    def decodeString(self, s):
        i = 0
        n = len(s)
        res = []
        while i < n:
            if "0" <= s[i] <= "9":
                tmp = ""
                while i < n and "0" <= s[i] <= "9":
                    tmp += s[i]
                    i += 1
                res.append(tmp)

            if s[i] == "[" or "a" <= s[i] <= "z":
                res.append(s[i])
            if s[i] == "]":
                tmp = ""
                while len(res) > 0 and res[-1] != "[":
                    tmp = res.pop(-1) + tmp
                res.pop(-1)
                num = res.pop(-1)
                tmp = int(num) * tmp
                res.append(tmp)
            i += 1
        return "".join(res)


# TinyURL是一种URL简化服务，
# 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
# 它将返回一个简化的URL http://tinyurl.com/4e9iAk.
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
# 你的加密和解密算法如何设计和运作是没有限制的，
# 你只需要保证一个URL可以被加密成一个TinyURL，
# 并且这个TinyURL可以用解密方法恢复成原本的URL。


# 给你一个未排序的整数数组nums ，请你找出其中没有出现的最小的正整数。

# 进阶：你可以实现时间复杂度为
# O(n)
# 并且只使用常数级别额外空间的解决方案吗？
# nums[i] <= n-1
##1....n
##0....n-1

##222222222
##0 。。。。n-1
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] > n - 1 or nums[i] < 0:
                continue
            ##把 1。。。。n的数字 放到对应的0。。。。n-1的位置
            while n >= nums[i] > 0 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for j in range(n):
            if nums[i] != j:
                return j
        return n


# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。
# 100
# 110
# 110
# 输入：grid = [[0,1],[1,0]]
# 输出：2
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
class Solution999:
    def shortestPathBinaryMatrix(self, grid):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1), (0, -1), (-1, 1), (-1, -1), (-1, 0)]
        t = len(grid)
        queue = [(0, 0, 1)]
        if grid[0][0] == 1 or grid[t - 1][t - 1] == 1:
            return -1
        while len(queue) != 0:
            m, n, l = queue.pop(0)
            if m == t - 1 and n == t - 1:
                return l
            for i, j in directions:
                nx, ny = m + i, n + j
                if nx >= 0 and nx <= t - 1 and ny >= 0 and ny <= t - 1 and grid[nx][ny] != 1:
                    queue.append((nx, ny, l + 1))
                    grid[nx][ny] = 1
        return -1


class Solution999:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        ##row_step = (0,1)
        ##col_step = (0,1)
        ## nums[i+row_step][j+col_step]
        step = 1
        row_position = 0
        col_position = 0
        self.min_step = float("inf")
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        visited = set()
        visited.add((0, 0))
        self.dfs(grid, step, row_position, col_position, n, visited)
        if self.min_step == float("inf"):
            return -1
        return self.min_step

    def dfs(self, grid, step, row_position, col_position, n, visited):
        if step > n * n or row_position > n - 1 or col_position > n - 1 or row_position < 0 or col_position < 0 or \
                grid[row_position][col_position] == 1:
            return
        if row_position == n - 1 and col_position == n - 1:
            self.min_step = min(self.min_step, step)
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i == 0 and j == 0:
                    continue
                if (row_position + i, col_position + j) not in visited:
                    visited.add((row_position + i, col_position + j))
                    self.dfs(grid, step + 1, row_position + i, col_position + j, n, visited)
                    visited.remove((row_position + i, col_position + j))


a = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]
s = Solution999()


# 给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，
# 先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3] 米，持续移动。
# 也就是说，每次移动后你的方位会发生逆时针变化。
# 编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。
# 示例 1:
# ┌───┐
# │   │
# └───┼──>
#    │

# 输入: [2,1,1,2]
# 输出: true
# 示例 2:
# ┌──────┐
# │      │
# │
# │
# └────────────>
# 输入: [1,2,3,4]
# 输出: false
# 示例 3:
# ┌───┐
# │   │
# └───┼>

# 输入: [1,1,1,1]
# 输出: true


class Solution132:
    def isSelfCrossing(self, distance):
        visited = set()
        index = 0
        position = (0, 0)
        visited.add(position)
        self.direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        self.flag = 0
        n = len(distance)
        self.dfs(index, position, visited, distance, n)
        if self.flag == 0:
            return False
        return True

    def dfs(self, index, position, visited, distance, n):
        if index == n:
            return
        direct = int(index % 4)
        new_position = position
        for j in range(1, distance[index] + 1):
            row_add = self.direction[direct][0] * j
            col_add = self.direction[direct][1] * j
            new_position = (position[0] + row_add, position[1] + col_add)
            if new_position in visited:
                self.flag = 1
                break
            else:
                visited.add(new_position)
        if self.flag == 1:
            return
        self.dfs(index + 1, new_position, visited, distance, n)


##print(s.isSelfCrossing([2,1,1,2]))


# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
# 输入：19
# 输出：true
# 解释：
# 1*1 + 9*9 = 82
# 8*8 + 2*2 = 68
# 6*6 + 8*8 = 100
# 1*1 + 0*0 + 0*0 = 1
##输入：n = 2
##输出：false
class Solution988:
    def isHappy(self, n):
        visited = set()
        tmp = str(n)
        while tmp != "1":
            if tmp in visited:
                return False
            visited.add(tmp)
            m = len(str(tmp))
            next = 0
            for i in range(m):
                next += int(tmp[i]) * int(tmp[i])
            tmp = str(next)
        return True


s = Solution988()


# print(s.isHappy(2))


##a-l1   a-l2
##           a
##        b      c
##      d   e  f    g
##   min , max
##

##a-e
##e-b, b-d

## b: ( min(left[1], root.left) , max(root.right,))


##设计一个敲击计数器，使它可以统计在过去5分钟内被敲击次数。
# 每个函数会接收一个时间戳参数（以秒为单位），你可以假设最早的时间戳从1开始，且都是按照时间顺序对系统进行调用（即时间戳是单调递增）。
# 在同一时刻有可能会有多次敲击。
# 示例:
# HitCounter counter = new HitCounter();
# // 在时刻 1 敲击一次。
# counter.hit(1);
# // 在时刻 2 敲击一次。
# counter.hit(2);
# // 在时刻 3 敲击一次。
# counter.hit(3);
# // 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
# counter.getHits(4);
# // 在时刻 300 敲击一次。
# counter.hit(300);
# // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
# counter.getHits(300);


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_hit_count = {}
        self.time_stamp = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.time_hit_count[timestamp] = self.time_hit_count.get(timestamp, 0) + 1
        k = int(timestamp / 300)
        if k not in self.time_stamp:
            self.time_stamp[k] = {timestamp}
        else:
            self.time_stamp[k].add(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        k = int(timestamp / 300)
        tmp = self.time_stamp.get(k - 1, set()) | self.time_stamp.get(k + 1, set()) | self.time_stamp.get(k, set())
        count = 0
        for i in tmp:
            if 0 <= timestamp - i < 300:
                count += self.time_hit_count[i]
        return count


##给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

# 示例2：
# 输入：s = "a", t = "a"
# 输出："a"

class Solution999:
    def minWindow(self, s, t):
        n = len(s)
        t_dict = {}
        t_set = set()
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
            t_set.add(i)
        l = 0
        begin = 0
        max_l = float("inf")
        if s == t:
            return t
        s_dict = {}
        for r in range(n):
            if s[r] in t_set:
                s_dict[s[r]] = s_dict.get(s[r], 0) + 1
                s_dict[s[r]] = min(s_dict[s[r]], t_dict[s[r]])
            while s_dict == t_dict and l <= r:
                if r - l + 1 < max_l:
                    max_l = r - l + 1
                    begin = l
                if s[l] in t_set:
                    s_dict[s[l]] = s_dict.get(s[l]) + 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                l += 1
        if max_l == float("inf"):
            return ""
        return s[begin:begin + max_l]


###请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。
# 这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
# 1 号机（发送方）有如下函数：
# string encode(vector<string> strs) {
#  // ... your code
#  return encoded_string;
# }
# 2 号机（接收方）有如下函数：

# vector<string> decode(string s) {
#  //... your code
#  return strs;
##1 号机（发送方）执行：
# string encoded_string = encode(strs);
# 2 号机（接收方）执行：
# vector<string> strs2 = decode(encoded_string);
##1 号机（发送方）执行：
# string encoded_string = encode(strs);
# 2 号机（接收方）执行：
# vector<string> strs2 = decode(encoded_string);
# ：
# 因为字符串可能会包含 256 个合法 ascii 字符中的任何字符，所以您的算法必须要能够处理任何可能会出现的字符。
# 请勿使用 “类成员”、“全局变量” 或 “静态变量” 来存储这些状态，您的编码和解码算法应该是非状态依赖的。
# 请不要依赖任何方法库，例如 eval 又或者是 serialize 之类的方法。本题的宗旨是需要您自己实现 “编码” 和 “解码” 算法。

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


##给定一组字符，使用原地算法将其压缩。
# 压缩后的长度必须始终小于或等于原数组长度。
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 在完成原地修改输入数组后，返回数组的新长度。
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
# 示例 1：
# 输入：
# ["a","a","b","b","c","c","c"]
# 输出：
# 返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 说明：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
##示例 2：
# 输入：
# ["a"]
# 输出：
# 返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 解释：
# 没有任何字符串被替代。
# 示例 3：
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 输出：
# 返回 4 ，输入数组的前4个字符应该是：["a","b","1","2"]。
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。

class Solution:
    def compress(self, chars) -> int:
        n = len(chars)
        i = 0
        index = 0
        while i < n:
            t = i
            count = 0
            tmp = chars[i]
            ## count
            while t < n and chars[t] == tmp:
                t += 1
                count += 1
            ##chars[j] != tmp
            if count == 1:
                chars[index] = tmp
                index += 1
                i += 1
            else:
                chars[index] = tmp
                index += 1
                count_string = str(count)
                for j in range(len(count_string)):
                    chars[index] = count_string[j]
                    index += 1
                i = t

        return index


##对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
# 示例 1：
# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
# 示例 2：
# 输入：asteroids = [8,-8]
# 输出：[]
# 解释：8 和 -8 碰撞后，两者都发生爆炸。
# 示例 3：
# 输入：asteroids = [10,2,-5]
# 输出：[10]
# 解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

class Solution13124:
    def asteroidCollision(self, asteroids):
        s = []
        n = len(asteroids)
        i = 0
        while i < n:
            if len(s) == 0:
                s.append(asteroids[i])
                i += 1
                continue
            if s[-1] > 0 and asteroids[i] < 0:
                if abs(s[-1]) > abs(asteroids[i]):
                    i += 1
                elif abs(s[-1]) == abs(asteroids[i]):
                    s.pop()
                    i += 1
                elif abs(s[-1]) < abs(asteroids[i]):
                    s.pop()
            else:
                s.append(asteroids[i])
                i += 1
        return s


s = Solution13124()


# print(s.asteroidCollision([-2, -1, 1, 2]))


##序列化是将一个数据结构或者对象转换为连续的比特位的操作，
# 进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 设计一个算法来实现二叉树的序列化与反序列化。
# 这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详
# 情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 示例 1：
##输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## 中左右 pre
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.pre_order(root)
        return "".join(self.res)

    def pre_order(self, root):
        if root is None:
            self.res.append("##")
            self.res.append(",")
            return
        self.res.append(str(root.val))
        self.res.append(",")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def deserialize(self, data):
        data = data.split(",")
        return self.help(data)

    def help(self, data):
        if data is None:
            return
        tmp = data.pop(0)
        if tmp == "##":
            return
        node = TreeNode(tmp)
        node.left = self.help(data)
        node.right = self.help(data)
        return node


root1 = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root1.left = root2
root1.right = root3
root3.left = root4
root3.right = root5

c = Codec()
# print(c.serialize(root1))
node = c.deserialize("1,2,##,##,3,4,##,##,5,##,##,")


##print(c.serialize(node))


##m=[1,2,4]
## 5
##  v | v-m(大) v-3 | v-2 | v-1
## j-w 较小的数值
## dp[j] = dp[j],dp[j-w]

##  v | v-m(小) v-1 | v-2 | v-3
## dp[j] = dp[j],dp[j-w]
## j- w : 较大的数值

class Solution3412:
    def intersect(self, nums1, nums2):
        num1 = sorted(nums1)
        num2 = sorted(nums2)
        i = 0
        j = 0
        res = []
        print(num1, num2)
        while i < len(num1) and j < len(num2):
            if num1[i] == num2[j]:
                res.append(num1[i])
                i += 1
                j += 1
            elif num1[i] < nums2[j]:
                i += 1
            elif num1[i] > nums2[j]:
                j += 1
        return res


# s = Solution3412()
# print(s.intersect([4,9,5], [9,4,9,8,4]))


##416. 分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意:
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:
# 输入: [1, 5, 11, 5]
# 输出: true
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 示例 2:
# 输入: [1, 2, 3, 5]
# 输出: false
# 解释: 数组不能分割成两个元素和相等的子集.
###

class Solution13124:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        k = int(total / 2)
        ##dp[0...k] = k
        ##dp[i] true
        ##dp[i] = dp[j] + i-j ,  in nums
        nums = sorted(nums)
        n = len(nums)
        ## 体重j能不能表示用前i个数字表示出来
        ##dp[i][j] = j-nums[t]==0 or dp[i-1][j-nums[t]] t<j
        dp = [[0 for i in range(k + 1)] for j in range(n)]
        for i in range(1, k + 1):
            for j in range(0, n):
                for m in range(j):
                    if i - nums[m] == 0 or dp[j - 1][i - nums[m]] == 1:
                        dp[i][j] = 1


# s = Solution13124()
# print(s.canPartition([1, 2, 5]))


class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        k = int(total / 2)
        n = len(nums)
        ##dp[0...k] = k
        ##dp[i] true
        ##dp[i] = dp[j] + i-j ,  in nums
        dp = [0 for i in range(k + 1)]
        dp[0] = 1
        for i in range(1, k + 1):
            flag = 0
            for num in nums:
                if i - num >= 0 and dp[i - num] == 1:
                    flag = 1
                    break
            dp[i] = flag
        return dp[k] == 1


class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        target = total // 2
        if maxNum > target:
            return False
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        ##target: 重量 n : 用不用的元素
        for j in range(1, target + 1):
            for i in range(1, n):
                num = nums[i]
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]


# 238. 除自身以外数组的乘积
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
# 示例:
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]


##977. 有序数组的平方
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 示例 1：
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
class Solution197:
    def missingNumber(self, nums):
        n = len(nums)
        flag = 0
        for i in range(n):
            if nums[i] == 0:
                flag = 1
                nums[i] = n + 1
        if flag == 0:
            return 0

        for i in range(n):
            index = abs(nums[i])
            if index == n:
                nums[0] = -abs(nums[0])
                continue
            if index == n + 1:
                nums[0] = -abs(nums[0])
                continue
            nums[index] = -abs(nums[index])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return n


class Solution981:
    def findAnagrams(self, s: str, p: str):
        s_dict = {}
        res = []
        for i in p:
            s_dict[i] = s_dict.get(i, 0) + 1
        m = len(s)
        n = len(p)
        if m < n:
            return res
        i = 0
        tmp_dict = {}
        for j in range(i, i + n - 1):
            tmp_dict[s[j]] = tmp_dict.get(s[j], 0) + 1
        while i < m - n + 1:
            print(i, n)
            tmp_dict[s[i + n - 1]] = tmp_dict.get(s[i + n - 1], 0) + 1
            print(tmp_dict)
            if tmp_dict == s_dict:
                res.append(i)
            tmp_dict[s[i]] -= 1
            if tmp_dict[s[i]] == 0:
                del tmp_dict[s[i]]
            i += 1
        return res


# s= Solution981()
# print(s.findAnagrams("cbaebabacd","abc"))


class Solution124129:
    def compress(self, chars):
        i = -1
        j = 0
        n = len(chars)
        tmp = 0
        while j < n:
            if i == -1:
                i += 1
                j += 1
                tmp = 1
            elif chars[i] == chars[j]:
                tmp += 1
                j += 1
            elif chars[i] != chars[j]:
                if tmp != 1:
                    tmp = str(tmp)
                    for t in range(len(tmp)):
                        i += 1
                        chars[i] = tmp[t]
                i += 1
                chars[i] = chars[j]
                tmp = 1
                j += 1
        if tmp != 1:
            tmp = str(tmp)
            for t in range(len(tmp)):
                i += 1
                chars[i] = tmp[t]
        return i + 1


##134. 加油站
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
# 说明:
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
# 示例 1:
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]


##如果 i到不了 j, 则 i---j 的 所有点都到不了，直接从j+1 开始找。
class Solution:
    def canCompleteCircuit(self, gas, cost):
        i = 0
        n = len(gas)
        while i < n:
            total_fuel = 0
            total_cost = 0
            count = 0
            while count < n:
                j = (i + count) % n
                total_fuel += gas[j]
                total_cost += cost[j]
                if total_fuel >= total_cost:
                    count += 1
                else:
                    break
            if count == n:
                return i
            i = i + count + 1
        return -1


# 284. 顶端迭代器
# 给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。
# 示例:
# 假设迭代器被初始化为列表 [1,2,3]。
# 调用 next() 返回 1，得到列表中的第一个元素。
# 现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
# 最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
## peak 返回 head
## next
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.index = 0
        self.nums = []
        while iterator.hasNext():
            self.nums.append(iterator.next())
        self.length = len(self.nums)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.index]

    def next(self):
        """
        :rtype: int
        """
        tmp = self.nums[self.index]
        self.index += 1
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.nums):
            return True
        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1240:
    def countUnivalSubtrees(self, root):
        self.count = 0
        if root is None:
            return self.count
        self.help(root)
        return self.count

    def help(self, root):
        if root is None:
            return True
        tmp1 = self.help(root.left)
        tmp2 = self.help(root.right)
        if tmp1 != True or tmp2 != True:
            return False
        if root.left != None and root.right != None:
            if root.val == root.left.val and root.val == root.right.val:
                self.count += 1
                return True
            else:
                return False
        elif root.left != None:
            if root.val == root.left.val:
                self.count += 1
                return True
            else:
                return False
        elif root.right != None:
            if root.val == root.right.val:
                self.count += 1
                return True
            else:
                return False
        else:
            self.count += 1
            return True


# 实现 LRUCache 类：
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，
# 则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
##输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4

class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity):
        self.key_val = {}
        self.tail = node(None)
        self.head = node(None)
        self.size = capacity

    def get(self, key: int):
        if key in self.key_val:
            val = self.key_val[key]
        self.move_to_head(key)
        return val

    def put(self, key: int, value: int):
        if key not in self.key_val:
            self.key_val[key] = value
            tmp = node(key)
            if self.head is None:
                self.head = tmp
                self.tail = tmp
            else:
                tmp.pre = self.tail
                self.tail.next = tmp
                self.tail = self.tail.next


# 907. 子数组的最小值之和
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
##示例 1：
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

##示例 2：
# 输入：arr = [11,81,94,43,3]
# 输出：444


##939. 最小面积矩形
# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。
# 如果没有任何矩形，就返回 0。
# 示例 1：
# 输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
# 示例 2：
# 输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2


#1436. 旅行终点站
#给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，
# 其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
# 请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
#题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

##SQL架构
#表1: Person
#+-------------+---------+
#| 列名         | 类型     |
#+-------------+---------+
#| PersonId    | int     |
#| FirstName   | varchar |
#| LastName    | varchar |
#+-------------+---------+
#PersonId 是上表主键
#表2: Address
#+-------------+---------+
#| 列名         | 类型    |
#+-------------+---------+
#| AddressId   | int     |
#| PersonId    | int     |
#| City        | varchar |
#| State       | varchar |
#+-------------+---------+
#AddressId 是上表主键
#编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，
#都需要基于上述两表提供 person 的以下信息：
#FirstName, LastName, City, State
##select a.FirstName,a.LastName,b.City,b.State
#from Person a join Address b on a.PersonId= b.PersonId


a= "Let's take LeetCode contest"
s = a.split(" ")
print(s)


class Solution1231:
    def permute(self, nums):
        self.res= []
        cur = []
        n = len(nums)
        self.nums = nums
        self.dfs(cur,n)
        return self.res
    def dfs(self,cur,n):
        if len(cur) == n :
            print(cur)
            if cur not in self.res:
                self.res.append(cur)
            return
        for num in self.nums:
            if num not in cur:
                self.dfs(cur + [num], n)  ## 这个是可以的
                ##cur.append(num)  这样写不行
                ##self.dfs(cur,n)   这个传的是 指针， cur pop 会影响
                ##cur.pop()         已经进去的元素

s = Solution1231()


class Solution115548:
    def longestPalindrome(self, s: str) -> str:
        #if s[i] =s[j]:
        #    dp[i][j] = dp[i+1][j-1]+1
        #else: dp[i][j]=0
        #i: 0...n
        #j:0:n
        #dp[0][0]=1
        #max(dp)
        n = len(s)
        dp =  [[0 for i in range(n)] for j in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j :
                    dp[i][j] = 1
                    continue
                if s[i] ==s[j]:
                    if j -i  <= 2:
                        dp[i][j] =j-i +1
                        continue
                    elif dp[i+1][j-1] != 0:
                        dp[i][j] = dp[i+1][j-1]+2
                    else:
                        dp[i][j]=0
                else:
                    dp[i][j]=0

        max_num = max([max(i) for i in dp])

        for i in range(n):
            for j in range(i,n):
                if dp[i][j] == max_num:
                    return s[i:j+1]

s= Solution115548()
print(s.longestPalindrome("cbbd"))