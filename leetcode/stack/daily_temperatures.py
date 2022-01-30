##请根据每日 气温 列表，重新生成一个列表。
# 对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

##   73   76   72,76  69
##   0    0    1       1


# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

class Solution1232:
    def dailyTemperatures(self, T):
        h = []
        n = len(T)
        time = [0 for i in range(n)]
        for i in range(n):
            while len(h) != 0 and h[-1][0] < T[i]:
                t, index = h.pop()
                time[index] = i-index
            h.append((T(i),i))
        return time

