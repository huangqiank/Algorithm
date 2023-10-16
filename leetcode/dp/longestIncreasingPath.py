##329. Longest Increasing Path in a Matrix
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
# Example 1:
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
import bisect
from collections import defaultdict
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.max_l = -float("inf")
        self.matrix = matrix
        for i in range(n):
            for j in range(m):
                self.max_l = max(self.max_l, self.dfs(i, j, n, m))
        return self.max_l

    @lru_cache(None)
    def dfs(self, i, j, n, m):
        best = 1
        for x, y in self.direction:
            new_x = i + x
            new_y = j + y
            if 0 <= new_x < n and 0 <= new_y < m and self.matrix[new_x][new_y] > self.matrix[i][j]:
                best = max(best, 1 + self.dfs(new_x, new_y, n, m))
        return best


class Solution2:
    def longestIncreasingPath(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix = matrix
        self.direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_l = 1
        for i in range(n):
            for j in range(m):
                self.visited = set()
                max_l = max(max_l, self.dfs(i, j, n, m))
        return max_l
    @lru_cache(None)
    def dfs(self, i, j, n, m):
        self.visited.add((i, j))
        max_l = 1
        for x, y, in self.direction:
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < n and 0 <= new_y < m:
                if (new_x, new_y) not in self.visited and self.matrix[new_x][new_y] > self.matrix[i][j]:
                    max_l = max(max_l, 1 + self.dfs(new_x, new_y, n, m))
        self.visited.remove((i, j))
        return max_l


s = Solution()
m = [[9,9,4],[6,6,8],[2,1,1]]



class Trie:
    def __init__(self):
        self.children = {}
        self.cnt =0
    def insert(self,word):
        s = self
        for w in word[::-1]:
            if w not in s.children:
                s.children[w] = Trie()
                s.cnt += 1
            s = s.children[w]
        s.cnt += 1

    def search(self,word):
        s = self
        for w in word[::-1]:
            if w not in s.children:
                return 0
            s = s.children[w]
        return s.cnt

class Solution13:

    def minimumLengthEncoding(self, words):
        t = Trie()
        res = 0
        for word in words:
            t.insert(word)
        for word in words:
            if t.search(word) == 1:
                res += len(word) + 1
        return res






class Solution134:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ##dp[i][j] = dp[i-1][j-1]+1, dp[i-1][j],dp[i][j-1]
        n = len(text1)
        m = len(text2)
        dp =[[0 for i in range(m)]for j in range(n)]
        ans =0
        if text1[0] == text2[0]:
            dp[0][0]= 1
        for i in range(1,m):
            if text1[0] == text2[i]:
                dp[0][i] = 1
                ans = 1
            else:
                dp[0][i] = dp[0][i-1]

        for i in range(1,n):
            if text1[i] == text2[0]:
                dp[i][0] = 1
                ans = 1
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1,n):
            for j in range(1,m):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                ans = max(ans,dp[i][j])

        return ans





class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution45:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        vec = []
        tmp = head
        while tmp:
            vec.append(tmp)
            tmp=tmp.next
        n = len(vec)
        i = 0
        pre = ListNode()
        while i < n-1-i:
            pre.next = vec[i]
            pre = pre.next
            pre.next = vec[n-1-i]
            pre = pre.next
            i+=1
        if i == n-1-i :
            pre.next = vec[i]
            pre = pre.next
        pre.next = None
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)


node1.next =node2
node2.next=node3
node3.next = node4

s =Solution45()
node = s.reorderList(node1)


class Solution123:
    def numSubarrayProductLessThanK(self, nums,k):
        pre = 1
        ans = 0
        pre_product = []
        for index, num in enumerate(nums):
            pre *= num
            if index == 0:
                if pre <=k :
                    ans +=1
                    print(num,ans)
                pre_product.append(pre)
                continue
            pre_index = bisect.bisect_left(pre_product, pre/k)
            if pre < k :
                ans += index + 1
            else:
                ans += index - pre_index
            print(num,ans)
            pre_product.append(pre)
        return ans

s=Solution123()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))

class Solution1234:
    def minSubArrayLen(self, target: int, nums):
        pre_sum= []
        pre =0
        ans = float("inf")
        for index, num in enumerate(nums):
            pre +=num
            if len(pre_sum) == 0 and  target < pre:
                ans = 1
            if target < pre and len(pre_sum) >0:
                pre_index =self.binary_search(pre_sum,pre - target)
                ans = min(ans,index-pre_index)
            if target == pre:
                ans = min(ans,index+1)
            pre_sum.append(pre)
        if ans == float("inf"):
            return 0
        return ans
    def binary_search(self,nums,target):
        left =0
        right= len(nums) -1
        while left +1 < right:
            mid = int((left + right)/2)
            if nums[mid] >= target:
                right = mid
            else:
                left =mid
        if nums[right] <= target:
            return right
        if nums[left] <= target:
            return left
        return -1
s= Solution1234()
print(s.minSubArrayLen(6,[10,2,3]))


##和为k 数组正负同时存在用前缀和哈希，只有正数用双指针

class Solution8:
    def dicesProbability(self, n: int) :
        dp = {1:1,2:1,3:1,4:1,5:1,6:1}
        for i in range(1,n):
            tmp = defaultdict(int)
            for k,v in dp.items():
                for j in range(1,7):
                    tmp[k+j] = dp.get(k,0) + tmp[k+j]
            dp = tmp

        total = sum(dp.values())
        return [dp[i]/total for i in sorted(list(dp.keys()))]














class FileSystem:
    def __init__(self):
        self.children = {}
        self.val = 0

    def insert(self,word,val):
        s = self
        for w  in word:
            if w not in s.children:
                s.children[w] = FileSystem()
            s = s.children[w]
            s.val +=val

    def check(self,word):
        if len(word) == 0:
            return True
        s = self
        for w in word:
            if w not in s.children:
                return False
            s = s.children[w]
        return True

    def get_val(self,word):
        s = self
        for w in word:
            if w not in s.children:
                return -1
            s = s.children[w]
        return s.val

    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path =="/":
            return False
        paths = path.split("/")[1:]
        for path in paths:
            if not path.isalpha():
                return False
        if self.check(paths[:-1]):
            self.insert(paths,value)
            return True
        return False


    def get(self, path: str) -> int:
        if path == "" or path =="/":
            return -1
        paths = path.split("/")[1:]
        for path in paths:
            if not path.isalpha():
                return -1
        return self.get_val(paths)
f = FileSystem()
f.createPath("/leet",1)
f.createPath("/leet/code",2)
f.get("/leet/code")
f.createPath("/leet/code",3)
print(f.get("/leet/code"))




class Solution:
    def calculate(self, s: str) -> int:
        pre=0
        n = len(s)
        tmp = ""
        res= []
        pre = "+"
        for i in range(n):
            if s[i].isdigit():
                tmp +=s[i]
            if s[i] in "+-*/":
                if pre == "+":
                    res.append(int(tmp))
                if pre == "-":
                    res.append( -int(tmp))
                if pre  =="*":
                    last=res.pop()
                    res.append(last*int(tmp))
                if pre == "/":
                    last=res.pop()
                    res.append(int(last/int(tmp)))
                pre =s[i]
                tmp = ""
        if pre == "+":
            res.append(int(tmp))
        if pre == "-":
            res.append( - int(tmp))
        if pre  =="*":
            last=res.pop()
            res.append(last*int(tmp))
        if pre == "/":
            last=res.pop()
            res.append(int(last/int(tmp)))
        return sum(res)
print(int(-3/2))

s= "  12  3  "
print(s.strip(" ").split(" "))














class Solution4:
    def numWays(self, n: int, k: int) -> int:
        if n==1:
            return k
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]
        dp1[0] = k
        dp1[1] = k
        dp2[0] = k
        dp2[1] = k * (k - 1)
        for i in range(2, n):
            dp1[i] = dp2[i - 1]
            dp2[i] = dp1[i - 1] * (k - 1) + dp2[i - 1] * (k - 1)
        return dp1[n - 1] + dp2[n - 1]


#11 12  21 22
#112 121 122 211 212 221
#1121 1211 1221 2111 2121 2211
#1122 1212 1222 2112 2122 2212





class solution2:
    def cal_num_bottle(self,n):
        cnt =0
        empty = n
        bottle = 0
        while empty >= 3  or bottle >0:
            cnt += bottle
            empty += bottle
            bottle = int(empty/3)
            empty = empty % 3
        if empty == 2:
            cnt+=1
        return cnt

s= solution2()
print(s.cal_num_bottle(94))


a = "9"
print(a.isdigit())
a="A"
print(a.isalpha())
a= "asda"
print(a[::-1])
print(int("00099"))
print(3 * [5])

a = [2,3]

print(2**3-1)
