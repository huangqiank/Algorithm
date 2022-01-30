
# 字符串S由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
# 同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

# 示例：

# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9, 7, 8]
# 解释：
# 划分结果为
# "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像
# "ababcbacadefegde", "hijhklij"
# 的划分是错误的，因为划分的片段数较少。


class Solution5:
    def partitionLabels(self, S: str):
        str_index = {}
        for i in range(len(S)):
            if S[i] not in str_index:
                str_index[S[i]] = [i]
            else:
                str_index[S[i]].append(i)
        all = []
        for i in list(str_index.values()):
            all.append((i[0], i[-1]))
        res = [all[0]]
        j = 1
        while j < len(all):
            start, end = res[-1]
            next_start, next_end = all[j]
            if len(res) > 0 and end > next_start and end < next_end:
                res.pop(-1)
                res.append((start, next_end))
            elif next_end > end:
                res.append((next_start, next_end))
            j += 1
        ans = [j - i + 1 for i, j in res]
        return ans

    ## i=0,j=1
    ## i[1]< j[0] stop
    ## i[1] > j[0] combine


s = Solution5()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
