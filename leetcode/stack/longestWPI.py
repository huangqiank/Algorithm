###1124. Longest Well-Performing Interval
# We are given hours, a list of the number of hours worked per day for a given employee.
# A day is considered to be a tiring day if and
# only if the number of hours worked is (strictly) greater than 8.
# A well-performing interval is an interval of days
# for which the number of tiring days is strictly larger than the number of non-tiring days.
# Return the length of the longest well-performing interval.
# Example 1:
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].

class Solution:
    def longestWPI(self, hours):
        scores = [1 if hour > 8 else -1 for hour in hours]
        n = len(hours)
        pre_sum = [0 for i in range(n+1)]
        pre_sum[0] = 0
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i - 1] + scores[i-1]
        ## pre_sum[j] - pre[i]>0 [i  j]
        stack = []
        for i in range(n):
            if len(stack) == 0 or pre_sum[stack[-1]] > pre_sum[i]:
                stack.append(i)
        j = n
        max_interval = 0
        while j > max_interval:
            while stack and pre_sum[j] > pre_sum[stack[-1]]:
                max_interval = max(max_interval, j - stack.pop())
            j -= 1
        return max_interval

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        # 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        # 倒序扫描数组，求最大长度坡
        i = n
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans


