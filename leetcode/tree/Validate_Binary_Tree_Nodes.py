##1361. Validate Binary Tree Nodes
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.
# Example 1:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild):
        ##[root]
        ## find the root
        ## visited   False
        ## n = n
        tmp = [0 for i in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                tmp[leftChild[i]] += 1
            if rightChild[i] != -1:
                tmp[rightChild[i]] += 1
        root = -1
        cnt = 0
        for i in range(n):
            if tmp[i] == 0:
                root = i
                cnt+=1
        if cnt > 1:
            return False
        if root ==-1:
            return False
        visited = set()
        this_level = [root]
        while this_level:
            n = len(this_level)
            while n > 0:
                node = this_level.pop(0)
                if node in visited:
                    return False
                visited.add(node)
                if leftChild[node]!= -1:
                    this_level.append(leftChild[node])
                if rightChild[node] != -1:
                    this_level.append(rightChild[node])
                n -= 1
        return len(visited) == n

s = Solution()
print(s.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,-1,-1,-1]))


class Solution2:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        node_degree = [0 for i in range(n)]
        i = 0
        while i < n:
            if leftChild[i] != -1:
                node_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                node_degree[rightChild[i]] += 1
            i += 1
        root = -1
        for i in range(n):
            if node_degree[i] == 0:
                root = i
                break
        if root == -1:
            return False
        seen = set()
        seen.add(root)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if leftChild[node] != - 1:
                if leftChild[node] in seen:
                    return False
                seen.add(leftChild[node])
                queue.append(leftChild[node])
            if rightChild[node] != - 1:
                if rightChild[node] in seen:
                    return False
                seen.add(rightChild[node])
                queue.append(rightChild[node])
        return len(seen) == n
