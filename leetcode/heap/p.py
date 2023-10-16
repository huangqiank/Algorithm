import heapq
from collections import defaultdict


class Solution:

    def topKFrequent(self, words, k):
        words_cnt = defaultdict(int)
        heap = []
        for word in words:
            words_cnt[word] += 1
        words = list(words_cnt.keys())
        for i in range(k):
            heap.append((words_cnt[words[i]], words[i]))
        heapq.heapify(heap)
        for i in range(k, len(words)):
            print(heap)
            if words_cnt[words[i]] > heap[0][0] or (words_cnt[words[i]] == heap[0][0] and words[i] < heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap, (words_cnt[words[i]], words[i]))
        heap = sorted(heap, key=lambda x: (-x[0], x[1]))
        res = []
        for cnt, word in heap:
            res.append(word)
        return res


s = Solution()
# print(s.topKFrequent(
# ["i","love","leetcode","i","love","coding"],3))
# print("leetcode" < "coding")
print(s.topKFrequent(["aaa", "aa", "a"], 2))


class Solution:
    def boundaryOfBinaryTree(self, root):
        if root and not root.left and not root.right: return [root.val]
        Left = []
        Bottom = []
        Right = []

        # 左边界
        def dfsLeft(root):
            if root and (root.left or root.right):
                Left.append(root.val)
                if root.left:
                    dfsLeft(root.left)
                else:
                    dfsLeft(root.right)

        # 底部叶子
        def dfsBottom(root):
            if root:
                if not root.left and not root.right:
                    Bottom.append(root.val)
                else:
                    dfsBottom(root.left)
                    dfsBottom(root.right)

        # 右边界
        def dfsRight(root):
            if root and (root.left or root.right):
                Right.append(root.val)
                if root.right:
                    dfsRight(root.right)
                else:
                    dfsRight(root.left)

        dfsLeft(root.left)
        dfsBottom(root)
        dfsRight(root.right)
        return [root.val] + Left + Bottom + Right[::-1]



class Solution123:
    def minInsertions(self, s):
        i = 0
        n = len(s)
        cnt = 0
        queue = []
        while i < n:
            if s[i] == "(":
                queue.append("(")
                i += 1
                continue
            if s[i] == ")":
                if i + 1 >= n:
                    if len(queue) > 0:
                        queue.pop()
                        cnt += 1
                    else:
                        cnt += 2
                elif s[i + 1] == ")":
                    if len(queue) > 0:
                        queue.pop()
                    else:
                        cnt += 1
                elif s[i + 1] == "(":
                    if len(queue) > 0:
                        cnt += 1
                    else:
                        queue.append("(")
                        cnt += 2
                i += 2
        cnt += 2 * len(queue)
        return cnt
s = Solution123()
print(s.minInsertions( ")())"))


#示例 1：







## root
##   root.pre(head)
##   root.tail()


class Solution33:
    def numOfWays(self, n):
        dif = 6
        same = 6
        for i in range(1,n) :
            next_dif = same*2 + dif *2
            next_same = 3*same + 2*dif
            dif,same = next_dif,next_same

        return (dif + same) % (10**9+7)


























#输出：1
#解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))" 。
#示例 2：
#输入：s = "())"
#输出：0
#解释：字符串已经平衡了。
#示例 3：
#输入：s = "))())("
#输出：3
#解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
#示例 4：
#输入：s = "(((((("
#输出：12
#解释：添加 12 个 ')' 得到平衡字符串。
#示例 5：
#输入：s = ")))))))"
#输出：5
#解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。


class Solution12:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild):
        node_set = set()
        i = 0
        node_set.add(0)
        while i < n:
            left, right = leftChild[i], rightChild[i]
            if left != -1 and left == right:
                return False
            if i not in node_set and left not in node_set and right not in node_set and (left != -1 or right != -1):
                return False
            if i in node_set and (left in node_set or right in node_set):
                return False
            if left not in node_set and left != - 1:
                node_set.add(left)
            if right not in node_set and right != -1:
                node_set.add(right)
            i += 1
        return True
s = Solution12()
print(s.validateBinaryTreeNodes(3,[1,-1,-1],[-1,-1,1]))










##给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。

#对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，修改后的链表不应该含有任何 0 。

#返回修改后链表的头节点 head 。

#示例 1：

#输入：head = [0,3,1,0,4,5,2,0]
#输出：[4,11]
#解释：
#上图表示输入的链表。修改后的链表包含：
#- 标记为绿色的节点之和：3 + 1 = 4
#- 标记为红色的节点之和：4 + 5 + 2 = 11




##你需要设计一个文件系统，你可以创建新的路径并将它们与不同的值关联。

#路径的格式是一个或多个连接在一起的字符串，形式为： / ，后面跟着一个或多个小写英文字母。例如， " /leetcode" 和 "/leetcode/problems" 是有效路径，而空字符串 "" 和 "/" 不是。

#实现 FileSystem 类:

#bool createPath(string path, int value) 创建一个新的 path ，并在可能的情况下关联一个 value ，然后返回 true 。如果路径已经存在或其父路径不存在，则返回 false 。
# int get(string path) 返回与 path 关联的值，如果路径不存在则返回 -1 。




##给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。
#列表中的每个元素只可能是整数或整数嵌套列表
#示例 1：
#输入：s = "324",
#输出：324
#解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
#示例 2：
#输入：s = "[123,[456,[789]]]",
#输出：[123,[456,[789]]]
#解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
#1. 一个 integer 包含值 123
#2. 一个包含两个元素的嵌套列表：
#    i.  一个 integer 包含值 456
#    ii. 一个包含一个元素的嵌套列表
#         a. 一个 integer 包含值 789









# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self)?""
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution888:
    def deserialize(self, s: str):
        stack= []
        i =0
        n =len(s)
        while i < n:
            if s[i].isdigit():
                tmp = ""
                while i< len(s) and s[i].isdigit():
                    tmp+= s[i]
                    i+=1
                stack.append(int(tmp))
            elif s[i] == ",":
                i+=1
            elif s[i] == "[":
                stack.append("[")
                i+=1
            elif s[i] == "]":
                tmp = []
                while stack[-1] != "[":
                    tmp.append(stack.pop())
                stack.pop()
                stack.append(tmp[::-1])
                i+=1
        return stack

s = Solution888()
print(s.deserialize("[123,[456,[789]]]"))

a ={}
a[(1,2,3,4)] = 1
print(a)
a[[1,2,3]]=1