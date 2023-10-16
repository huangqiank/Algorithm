# 6. Z 字形变换
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
import heapq
import itertools
from collections import deque, defaultdict
from functools import lru_cache

from caffe2.python.ideep.transform_ideep_net import pairwise


class Solution:
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        res = ["" for i in range(numRows)]
        i = 0
        direction = 1
        for word in s:
            res[i] += word
            i += direction
            if i == numRows - 1 or i == 0:
                direction = -direction
        return "".join(res)



class Solution123:
    def alienOrder(self, words):
        def init_graph():
            g, n = defaultdict(set), len(words)
            for i in range(n - 1):
                word0, word1 = words[i], words[i + 1]
                n0, n1 = len(word0), len(word1)
                # 形如["abc", "ab"]的样例是违反定义的, 特殊判断
                if n0 > n1 and word0[:n1] == word1:
                    return None

                m = min(n0, n1)
                for j in range(m):
                    if word0[j] == word1[j]:
                        continue
                    # 第一对不同的字符提供序关系, 后面的字符忽略
                    g[word0[j]].add(word1[j])
                    break
            return g

        def count_in_degree(g):
            degree = {}
            # 将出现字符的入度初始化为0
            for word in words:
                for ch in word:
                    degree[ch] = 0

            for char, charset in g.items():
                for ch in charset:
                    degree[ch] += 1
            return degree

        g = init_graph()
        if g is None:
            return ""
        in_degree = count_in_degree(g)


        queue, count = deque(), 0
        for char, degree in in_degree.items():
            count += 1
            if degree == 0:
                queue.append(char)

        order = ""
        while queue:
            ch = queue.popleft()
            order += ch

            if ch in g:
                for c in g[ch]:
                    in_degree[c] -= 1
                    if in_degree[c] == 0:
                        queue.append(c)
        return order if len(order) == count else ""







class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution131:
    def cutOffTree(self, forest):
        self.index_value = []
        n = len(forest)
        m = len(forest[0])
        for i in range(n):
            for j in range(m):
                if forest[i][j] != 0:
                    self.index_value.append((i, j, forest[i][j]))
        self.index_value = sorted(self.index_value, key=lambda x: x[2])
        total = 0
        print(self.index_value)

        self.index_value = [(0,0,11)] + self.index_value
        for i in range(len(self.index_value) - 1):
            a, b, v1 = self.index_value[i]
            c, d, v2 = self.index_value[i + 1]
            self.visit = [[-1 for i in range(m)] for j in range(n)]
            self.visit[a][b] = 1
            step = self.check(a, b, c, d, n, m, forest)
            if step == -1:
                return -1
            total += step
        return total

    def check(self, a, b, c, d, l, m, forest):
        queue = deque([(a, b)])
        step = 0
        while queue:
            n = len(queue)
            while n > 0:
                n -= 1
                a, b = queue.popleft()
                if a == c and b == d:
                    return step
                for x, y in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                    if 0 <= x < l and 0 <= y < m and forest[x][y] != 0 and self.visit[x][y] == -1:
                        self.visit[x][y] = 1
                        queue.append((x, y))
            step += 1
        return -1


class Solution8:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        pre = [ 0 for i in range(col)]
        res = 0
        for i in range(row):
            for j in range(col):
                pre[j]  = pre[j]+1 if matrix[i][j] == "1" else 0
            stack = []
            l = []
            for i in range(col):
                if len(stack) ==0 :
                    stack.append(i)
                    l.append(-1)
                    continue
                while len(stack) > 0 and pre[stack[-1]] >=  pre[i]:
                    stack.pop()
                if len(stack) == 0 :
                    l.append(-1)
                else:
                    l.append(stack[-1])
                stack.append(i)
            stack= []
            r =[ ]
            for i in range(col-1,-1,-1):
                if len(stack) ==0 :
                    stack.append(i)
                    r.append(col)
                    continue
                while len(stack) > 0 and pre[stack[-1]] >=  pre[i]:
                    stack.pop()
                if len(stack) == 0 :
                    r.append(col)
                else:
                    r.append(stack[-1])
                stack.append(i)
            ans = 0
            r = r[::-1]
            for i in range(col):
                ans = max(ans,(r[i]-l[i]-1) * pre[i])
            print(pre,l,r,ans)
            res= max(ans,res)
        return res
s = Solution8()
a = [["0","1"],["1","0"]]
print(s.maximalRectangle(a))