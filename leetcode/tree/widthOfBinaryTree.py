##给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

# 示例 1:
# 输入:

#           1
#         /   \
#        3     2
#       / \     \
#      5   3     9

# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 示例 2:

# 输入:

#          1
#         /
#        3
#       / \
#      5   3

# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
# 示例 3:

# 输入:

#         1
#         / \
#        3   2
#       /
#      5

# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
# 示例 4:

# 输入:

#          1
#         / \
#        3   2
#       /     \
#      5       9
#     /         \
#    6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        next_level = [[root, 0]]
        max_w = 0
        while next_level:
            arr = []
            n = len(next_level)
            while n > 0:
                n -= 1
                node, pos = next_level.pop(0)
                arr.append(pos)
                if node.left:
                    next_level.append([node.left, 2 * pos])
                if node.right:
                    next_level.append([node.right, 2 * pos + 1])
            max_w = max(max_w, arr[-1] - arr[0] + 1)
        return max_w

# 示例 1:
# 输入:

#           1
#         /   \
#        3     2
#       / \     \
#      5   3     9

# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 示例 2:




##给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。

#UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

#对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
#对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
#这是 UTF-8 编码的工作方式：

#   Char. number range  |        UTF-8 octet sequence
#      (hexadecimal)    |              (binary)
#   --------------------+---------------------------------------------
#   0000 0000-0000 007F | 0xxxxxxx
#   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。



#示例 1：

#输入：data = [197,130,1]
#输出：true
#解释：数据表示字节序列:11000101 10000010 00000001。
#这是有效的 utf-8 编码，为一个 2 字节字符，跟着一个 1 字节字符。
#示例 2：


#class Solution:
 #   def validUtf8(self, data: List[int]) -> bool: