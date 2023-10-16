##Given a linked list,
##return the node where the cycle begins. If there is no cycle,
##return null.
##To represent a cycle in the given linked list,
##we use an integer pos which represents the position (0-indexed) in the linked list
##where tail connects to. If pos is -1, then there is no cycle in the linked list.
##Note: Do not modify the linked list.
##Example 1:
##Input: head = [3,2,0,-4], pos = 1
##Output: tail connects to node index 1
##Explanation: There is a cycle in the linked list, where tail connects to the second node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    slow = head
    quick = head

    while True:
        if quick or quick.next or quick.next.next:
            return None
        slow = slow.next
        quick = quick.next.next
        if slow == quick:
            break
    new = head
    while slow:
        if slow == new:
            return new
        new = new.next
        slow = slow.next




class Solution12:
    def findNumberOfLIS(self, nums):
        #dp[n] = (n,cnt)
        n = len(nums)
        dp =[[1,1] for i in range(n)]
        max_l= 0
        for i in range(n):
            x, y = dp[i]
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > x:
                        x =dp[j][0] + 1
                        y = dp[j][1]
                    elif dp[j][0] +1 == x:
                        y  += dp[j][1]
            dp[i] =[x,y]
            max_l = max(x,max_l)
        cnt = 0
        print(dp,max_l)
        for i in range(n):
            if dp[i][0] == max_l:
                cnt += dp[i][1]
        return cnt
s = Solution12()



class Solution141:
    def maxAreaOfIsland(self, grid):
        self.visit = set()
        self.direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.n = n = len(grid)
        self.m = m = len(grid[0])
        self.grid = grid
        max_area = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in self.visit and grid[i][j] == 1:
                    self.area = 0
                    self.visit.add((i, j))
                    self.dfs(i, j)
                    max_area = max(max_area,self.area)
        return max_area

    def dfs(self, x, y):
        self.area +=1
        for i, j in self.direction:
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < self.n and 0 <= new_y < self.m and (new_x, new_y) not in self.visit and self.grid[new_x][
                new_y] == 1:
                self.visit.add((new_x, new_y))
                self.dfs(new_x, new_y)


a = [[0,1,1],[1,1,0]]

s = Solution141()
print(s.maxAreaOfIsland(a))