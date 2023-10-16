##449. 序列化和反序列化二叉搜索树
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
# 编码的字符串应尽可能紧凑。
# 示例 1：
# 输入：root = [2,1,3]
# 输出：[2,1,3]
# 示例 2：
# 输入：root = []
# 输出：[]

# Definition for a binary tree node.
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        self.res = ""
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.res += ","
        self.res += str(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        data = data.split(",")
        data.pop(0)
        preorder = [int(i) for i in data]
        inorder = sorted(preorder)
        self.inorder_dict = {i: index for index, i in enumerate(inorder)}
        pre_start, pre_end, inorder_start, inorder_end = 0, len(preorder), 0, len(inorder)
        return self.construct(preorder, pre_start, pre_end, inorder, inorder_start, inorder_end)

    def construct(self, preorder, pre_start, pre_end, inorder, inorder_start, inorder_end):
        if pre_start == pre_end:
            return None
        val = preorder[pre_start]
        index = self.inorder_dict[val]
        left_num = index - inorder_start
        root = TreeNode(val)
        root.left = self.construct(preorder, pre_start + 1, pre_start + 1 + left_num, inorder, inorder_start, index)
        root.right = self.construct(preorder, pre_start + 1 + left_num, pre_end, inorder, index + 1, inorder_end)
        return root


class Codec2:
    ## left right mid
    def serialize(self, root):
        stack = []
        res = ""
        pre = None
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                if root.right is None or root.right == pre:
                    res = res + "," + str(root.val)
                    pre = root
                    root = None
                else:
                    stack.append(root)
                    root = root.right

        return res

    ## 左中右， 左右中
    def deserialize(self, data):
        data = data.split(",")
        data.pop(0)
        self.postorder = [int(i) for i in data]
        min_value = -float("inf")
        max_value = float("inf")
        return self.construct(min_value, max_value)

    def construct(self,  min_value, max_value):
        if not self.postorder or self.postorder[-1] < min_value or self.postorder[-1] > max_value:
            return None
        root= TreeNode(self.postorder.pop())
        root.right = self.construct(root.val, max_value)
        root.left = self.construct(min_value, root.val)
        return root


treenode1 = TreeNode(2)
treenode2 = TreeNode(1)
treenode3 = TreeNode(31)
treenode1.left = treenode2
treenode1.right = treenode3
c = Codec2()




##    def deserialize(self, data: str):

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
treenode1 = TreeNode(2)
treenode2 = TreeNode(1)
treenode3 = TreeNode(3)
treenode1.left = treenode2
treenode1.right = treenode3
#a = [[1,2],[3,4]]
#[a[0][0]a[1][0]]


class Solution123:
    def waysToSplit(self, nums):
        # pre =[]
        # [i k j ]
        ##  nums[j]>=2*nums[k]   ans nums[k] > 2*nums[i]
        pre = []
        for num in nums:
            if len(pre) == 0:
                pre.append(num)
            else:
                pre.append(pre[-1] + num)
        cnt = 0
        n = len(pre)
        for index in range(n - 2):
            # 2*pre[index] <= pre[i] <= (pre[-1] +pre[index])

            a = self.binary_search(pre, 2 * pre[index])
            a = max(a,index+1)
            b = self.binary_search2(pre, (pre[-1] + pre[index]) / 2)
            b = min(n-2,b)
            if b >=a:
                cnt += b - a + 1
        return cnt


    def binary_search2(self, nums, k):
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = int((l + r) / 2)
            if nums[mid] > k:
                r = mid
            else:
                l = mid
        if nums[r] <= k:
            return r
        return l

    def binary_search(self, nums, k):
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = int((l + r) / 2)
            if nums[mid] >= k:
                r = mid
            else:
                l = mid
        if nums[l] >= k:
            return l
        return r


s = Solution123()
print(s.waysToSplit([0,3,3]))

