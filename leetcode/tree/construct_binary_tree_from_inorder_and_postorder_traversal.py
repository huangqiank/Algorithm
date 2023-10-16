##Given inorder and postorder traversal of a tree, construct the binary tree.
##Note:
##You may assume that duplicates do not exist in the tree.
##For example, given
##inorder = [9,3,15,20,7]
##左中右
##postorder = [9,15,7,20,3]
##左右中
##倒着来中右左
##post[3,20,7,15,9]
##in[9,3,15,20,7]
##Return the following binary tree:
##    3
##   / \
##  9  20
##    /  \
##  15   7

# Definition for a binary tree node.
##[9,3,15,20,7]
##[9], [3], [15,20,7]
##
## 左边的数量： index - start
## 右边的数量： in_end - index-1
##总数： in_end -start-1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## left mid right
##  mid right left
class Solution:
    def buildTree(self, inorder, postorder):
        postorder.reverse()
        inorder_map = {value: index for index, value in enumerate(inorder)}
        self.buildTree_help(inorder_map, inorder, 0, len(inorder), postorder, 0, len(postorder))

    def buildTree_help(self, inorder_map, inorder, in_start, in_end, postorder, post_start, post_end):
        if post_start >= post_end or in_start >= in_end:
            return None
        root_val = postorder[post_start]
        root = TreeNode(root_val)
        index = inorder_map[root_val]
        ##为什么减一？？？？
        ##用inorder 的数目计算出来的
        right_num = in_end - index - 1
        root.right = self.buildTree_help(inorder_map, inorder, index + 1, in_end, postorder,
                                         post_start + 1, post_start + right_num + 1)
        root.left = self.buildTree_help(inorder_map, inorder, in_start, index, postorder,
                                        post_start + right_num + 1, post_end)
        return root


## 左边的数量： index - start
## 右边的数量： in_end - index-1
##总数： in_end -start-1

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
s = Solution()
print(s.buildTree(inorder, postorder))

## inorder : 左中右
## postorder 左右中
