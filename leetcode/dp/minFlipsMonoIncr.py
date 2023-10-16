##926. Flip String to Monotone Increasing
# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.
# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

class Solution:
    def minFlipsMonoIncr(self, s):
        # s[i] == 1   #dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        ##            dp[i][0] = dp[i-1][0]+1
        ##s[i] == 0  ##dp[i][1] = 1+ min(dp[i-1][0], dp[i-1][1])
        ##            dp[i][0] = dp[i-1][0]
        n = len(s)
        dp = [[float("inf") for i in range(2)] for j in range(n)]
        if n == 0:
            return 0
        if s[0] == "0":
            dp[0][0] = 0
            dp[0][1] = 1
        else:
            dp[0][0] = 1
            dp[0][1] = 0
        for i in range(1, n):
            if s[i] == "1":
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][1] = 1 + min(dp[i - 1][0], dp[i - 1][1])
                dp[i][0] = dp[i - 1][0]
        return min(dp[n - 1][0], dp[n - 1][1])


s = Solution()
print(s.minFlipsMonoIncr("010110"))


class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        ## 00001111
        ## s[i]:
        ##i-1
        ## presum[i] +  (n-i- (total- presun[i]))
        ## 2*presum[i] + n-i -total
        n = len(s)
        presum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            if s[i - 1] == "0":
                presum[i] = presum[i - 1]
            else:
                presum[i] = presum[i - 1] + 1
        total = presum[n]
        max_n = float("inf")
        for i in range(n + 1):
            max_n = min(max_n, 2 * presum[i] + n - i - total)
        return max_n


s = Solution2()
print(s.minFlipsMonoIncr("00011000"))



##Design a Leaderboard class, which has 3 functions:

#addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
#top(K): Return the score sum of the top K players.
#reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
#Initially, the leaderboard is empty.
##Input:
#["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
#[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
#Output:
#[null,null,null,null,null,null,73,null,null,null,141]


class Node:
    def __init__(self, index, val):
        self.pre = None
        self.next = None
        self.val = val
        self.index = index


class Leaderboard:

    def __init__(self):
        self.id_node = {}
        self.head = Node(0, -float("inf"))
        self.tail = Node(0, float("inf"))
        self.head.next = self.tail
        self.tail.pre = self.head

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.id_node:
            node = self.id_node[playerId]
            node.val += score
            node.pre.next = node.next
            node.next.pre = node.pre
        else:
            node = Node(playerId, score)
        self.place(node)
        self.id_node[playerId] = node

    def place(self, node):
        tmp = self.head.next
        flag = 0
        while tmp != self.tail:
            if tmp.val > node.val:
                flag = 1
                node.pre = tmp.pre
                node.next = tmp
                tmp.pre.next = node
                tmp.pre =node
                break
            tmp = tmp.next
        if flag == 0:
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre.next = node
            self.tail.pre = node

    def top(self, K: int) -> int:
        tmp = self.tail.pre
        total = 0
        while tmp != self.head and K > 0:
            total += tmp.val
            K -= 1
            tmp = tmp.pre
        return total

    def reset(self, playerId: int) -> None:
        if playerId not in self.id_node:
            return
        node = self.id_node[playerId]
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.id_node[playerId]

l=Leaderboard()
l.addScore(1,73)
l.addScore(2,56)
l.addScore(3,39)
l.addScore(4,51)
l.addScore(5,4)
tmp = l.head.next
while tmp != l.tail:
    print(tmp.index,tmp.val,tmp.pre.val)
    tmp = tmp.next

l.reset(1)
tmp = l.head
while tmp != l.tail:
    print(tmp.index,tmp.val)
    tmp = tmp.next

l.reset(2)
l.addScore(2,51)
print(l.top(3))




##You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

#We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

#We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

#Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

#For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
#Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
#Example 1:
#Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
#Output: 6
#Explanation:
#The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
#Notice that book number 2 does not have to be on the first shelf.

#class Solution:
#    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        ##[ai,bi]
        ## [] [] [] [] []
        ##stack [a,a,a,,],[b,b,b,], [c,c,c] , [d,d,d] , [] , []
        ## max_h[]    []   []  ,[]