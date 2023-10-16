##Given a linked list, determine if it has a cycle in it.
##To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed) in the linked list
# where tail connects to. If pos is -1, then there is no cycle in the linked list.
##Example 1:
##Input: head = [3,2,0,-4], pos = 1
##Output: true
##Explanation: There is a cycle in the linked list, where tail connects to the second node.
##Example 2:
##Input: head = [1,2], pos = 0
##Output: true
##Explanation: There is a cycle in the linked list, where tail connects to the first node.
##Example 3:

##Input: head = [1], pos = -1
##Output: false
##Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        if not head:
            return False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Solution12:
    def maxHeight(self, cuboids):
        for cuboid in cuboids:
            cuboid.sort()
        cuboids = sorted(cuboids)
        n = len(cuboids)
        dp = [cuboids[i][2] for i in range(n)]
        for i in range(1, n):
            x, y, z = cuboids[i]
            for j in range(i):
                a, b, c = cuboids[j]
                if a <= x and b <= y and c <= z:
                    dp[i] = max(dp[j] + z, dp[i])
        return max(dp)

s = Solution12()
cuboids =[[35,32,11],[7,6,65],[3,39,41]]
print(s.maxHeight(cuboids))
##65

print(cuboids[0:-2])
