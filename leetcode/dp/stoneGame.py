##877. Stone Game
# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row,
# and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.
#  The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first.
#  Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row.
#  This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
# Example 1:
# Input: piles = [5,3,4,5]
# Output: true
# Explanation:
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
from collections import defaultdict


class Solution:
    def stoneGame(self, piles) -> bool:
        nums = piles
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 1):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

    ## nums[0] - dp[1][n-1]
    ## nums[n-1] - dp[0][n-2]
    ##dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] -dp[i][j-1])
    class Solution:
        def stoneGame(self, piles):
            n = len(piles)
            dp = [[0 for i in range(n)] for j in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i , n):
                    if  i == j :
                        dp[i][i] = piles[i]
                    else:
                        dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
            return dp[0][n-1] >= 0


##Alice and Bob take turns playing a game, with Alice starting first.
#There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining
#  stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
#Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference.
# Alice's goal is to maximize the difference in the score.
#Given an array of integers stones where stones[i] represents the value of the ith stone from the left,
#  return the difference in Alice and Bob's score if they both play optimally.
##Input: stones = [5,3,1,4,2]
#Output: 6
#Explanation:
#- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
#- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
#- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
#- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
#- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
#The score difference is 18 - 12 = 6.


class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        pre_sum = [0 for i in range(1 + n)]
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + stones[i - 1]
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(pre_sum[j + 1] - pre_sum[i+1]  - dp[i + 1][j],
                               pre_sum[j] - pre_sum[i] - dp[i][j - 1])
        return dp[0][n - 1]


##1686. Stone Game VI
#Alice and Bob take turns playing a game, with Alice starting first.
#There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.
#You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.
#The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.
#Determine the result of the game, and:
#If Alice wins, return 1.
#If Bob wins, return -1.
#If the game results in a draw, return 0.
#Example 1:
#Input: aliceValues = [1,3], bobValues = [2,1]
#Output: 1
#Explanation:
#If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
#Bob can only choose stone 0, and will only receive 2 points.
#Alice wins.

class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        tmp = []
        n = len(aliceValues)
        for i in range(n):
            tmp.append([aliceValues[i] + bobValues[i], i])
        tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
        alice_total = 0
        bob_total = 0
        for i in range(n):
            if i % 2 == 0:
                alice_total += aliceValues[tmp[i][1]]
            else:
                bob_total += bobValues[tmp[i][1]]
        if alice_total > bob_total:
            return 1
        if alice_total == bob_total:
            return 0
        return -1


##1872. Stone Game VIII
#Alice and Bob take turns playing a game, with Alice starting first.
#There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:
#Choose an integer x > 1, and remove the leftmost x stones from the row.
#Add the sum of the removed stones' values to the player's score.
#Place a new stone, whose value is equal to that sum, on the left side of the row.
#The game stops when only one stone is left in the row.
#The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.
#Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.
#Example 1:

#Input: stones = [-1,2,-3,4,-5]
#Output: 5
#Explanation:
#- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
#  value 2 on the left. stones = [2,-5].
#- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
#  the left. stones = [-3].
#The difference between their scores is 2 - (-3) = 5.
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        #f(i,j) = f(i+1,j)
        #f(i,j) = pre(i) - f(i+1,j)
        n = len(stones)
        dp = [-float("inf") for i in range(n)]
        pre= [0 for i in range(n+1)]
        for i in range(1,n+1):
            pre[i] = pre[i-1] + stones[i-1]
        ## i i+1....   j
        dp[n-1] = pre[n]
        if n==2:
            return pre[2]
        if n<2:
            return 0
        for i in range(n-2,0,-1):
            dp[i] = max(pre[i+1]- dp[i+1],dp[i+1])
        return max(dp)
