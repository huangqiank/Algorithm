##297. 二叉树的序列化与反序列化
##序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
##请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
##示例 1：
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


##dfs
class Codec:
    ##mid left right
    def serialize(self, root):
        self.res = []
        self.preorder(root)
        return ",".join(self.res)

    def preorder(self, root):
        if not root:
            self.res.append("x")
            return
        self.res.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

    def deserialize(self, data):
        data = data.split(",")
        if len(data) == 0:
            return None
        root = self.construct(data)
        return root

    def construct(self, data):
        if len(data) == 0:
            return
        val = data.pop(0)
        if val == "x":
            return None
        new = TreeNode(int(val))
        new.left = self.construct(data)
        new.right = self.construct(data)
        return new


class Codec3:
    def serialize(self, root):
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("x")
        return ",".join(res)

    def deserialize(self, data):
        if data =="x":
            return None
        data = data.split(",")
        index = 1
        root = TreeNode(int(data[0]))
        queue = [root]
        while index < len(data):
            tmp = queue.pop(0)
            if data[index] != "x":
                left = TreeNode(data[index])
                tmp.left = left
                queue.append(left)
            if data[index + 1] != "x":
                right = TreeNode(data[index+1])
                tmp.right = right
                queue.append(right)
            index += 2
        return root


treenode1 = TreeNode(2)
treenode2 = TreeNode(1)
treenode3 = TreeNode(31)
treenode1.left = treenode2
treenode1.right = treenode3
c = Codec3()

t = c.deserialize(c.serialize(treenode1))
print(t.val)
print(t.left.val)
print(t.right.val)
