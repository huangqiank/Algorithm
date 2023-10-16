##403. Frog Jump
# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
# Example 1:
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
from functools import lru_cache


class Solution:
    def canCross(self, stones):
        n = len(stones)
        dp = [[0 for i in range(n)] for i in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                if dp[j][k - 1] == 1 or dp[j][k + 1] == 1 or dp[j][k] == 1:
                    dp[i][k] = 1
                if i == n - 1 and dp[i][k] == 1:
                    return True
        return False


class Solution2:
    def canCross(self, stones):
        self.stones = stones
        self.stone_set = set(stones)
        return self.dfs(0, 0)

    @lru_cache(None)
    def dfs(self, pos, step):
        if pos == self.stones[-1]:
            return True
        for d in [-1, 0, 1]:
            if step + d > 0 and pos + step + d in self.stone_set:
                if self.dfs(pos + step + d, step + d):
                    return True
        return False


class Solution3:
    def canCross(self, stones):
        stones_set = set(stones)
        dp = defaultdict(set)
        dp[0] = {0}
        for s in stones:
            for step in dp[s]:
                for d in [-1, 0, 1]:
                    if step + d > 0 and s + step + d in stones_set:
                        dp[s + step + d].add(step + d)
        return len(dp[stones[-1]]) >= 1

n =123

print(n%10)
n = int(n/10)
print(n%10)