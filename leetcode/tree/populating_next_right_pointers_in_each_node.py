##You are given a perfect binary tree where all leaves are on the same level,
##and every parent has two children. The binary tree has the following definition:
# struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
# }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Example:
# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

# Explanation: Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node, just like in Figure B.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root):
        if not root:
            return
        cur = root
        while cur:
            dummy = Node(0)
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
        return root

    def connect2(self, root):
        if not root:
            return root
        stack = [[root]]
        while stack:
            this_level = stack.pop(0)
            tmp = []
            for i in range(0, len(this_level) - 1):
                this_level[i].next = this_level[i + 1]
            for node in this_level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if len(tmp) > 0:
                stack.append(tmp)
        return root


class Solution23():
    def nextGreaterElement(self, n: int) -> int:
        num_str = str(n)
        nums = [int(num_str[i]) for i in range(len(num_str))]
        stack = []
        n = len(nums)
        res = [-1 for i in range(n)]
        swap_index = -1
        for i in range(n):
            print(stack)
            if len(stack) == 0 or nums[stack[-1]] >= nums[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                    index = stack.pop()
                    res[index] = i
                    swap_index = index
                stack.append(i)
        if swap_index == -1:
            return -1
        another_swap_index = res[swap_index]
        small = nums[another_swap_index]
        for i in range(res[swap_index], n):
            if nums[swap_index] < nums[i] <= small:
                small = nums[i]
                another_swap_index = i
        nums[another_swap_index], nums[swap_index] = nums[swap_index], nums[another_swap_index]
        nums = nums[:swap_index + 1] + sorted(nums[swap_index + 1:])
        return int("".join([str(num) for num in nums]))


s = Solution23()
s = "11:11"
print(s.split(":"))
print("a".isalpha())
print(3 * "a")
a = {1: 3}
del a[1]
print(a)
a = ["ad", "mf", "bv"]
print(sorted(a))
print(ord("a"))
print(ord("Z"))
print(ord("A"))  ##32
print(chr(ord("A") + 32))
print(3 * ("".join(["a", "b"][::-1])))

# ord chr
print(a[0:])
print(a[0:-2])
print(a[::-1])


class Solution21:
    def findLengthOfShortestSubarray(self, arr) -> int:
        left = 0
        right = len(arr) - 1
        n = len(arr)
        ##3212341
        while left + 1 < len(arr) and arr[left] <= arr[left + 1]:
            left += 1
        ### left : 0.... n-1

        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1
        ## right : n-1......0
        if left >= right:
            return 0
        print(left, right)
        result = min(n - left - 1, right)

        i = 0  ## can be choosed
        j = right  ##  can be choosed

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        return result


s = Solution21()
print(s.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
print(ord("a"))
print(chr(97))
s = "adaf"

remain_counter = collections.Counter(s)
print(remain_counter)
print(s[0:2])
a = [1, 2, 3, 4, 4]


class Solutionq1145:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        stack = []
        stack.append((0, 0))
        visited = set()
        visited.add((0,0))
        step = 0
        while stack:
            n = len(stack)
            while n > 0:
                n -= 1
                index, flag = stack.pop(0)
                if index == x:
                    return step
                if index + a < 6000 and (index + a, 0) not in visited and index + a not in forbidden:
                    visited.add((index+a, 0))
                    stack.append((index + a, 0))
                if flag == 0 and index - b >= 0 and (index - b, -1) not in visited and index - b not in forbidden:
                    visited.add((index - b , -1))
                    stack.append((index - b, -1))
            step += 1
        return -1


s = Solutionq1145()
forbidden = [8, 3, 16, 6, 12, 20]
a = 15
b = 13
x = 11
print(s.minimumJumps(forbidden, a, b, x))



class Solution:
    def findSubsequences(self, nums):
        self.res= []
        tmp = []
        self.dfs(0,tmp,nums)
        return self.res

    def dfs(self,index,tmp,nums):
        if index == len(nums):
            if len(tmp) >= 2 and tmp not in self.res:
                self.res.append(tmp)
            return
        if len(tmp) > 0 and tmp[-1] > nums[index]:
            self.dfs(index+1, tmp, nums)
        else:
            self.dfs(index+1, tmp + [nums[index]], nums)
            self.dfs(index+1, tmp, nums)


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

































class Solution713:
    def firstDayBeenInAllRooms(self, nextVisit):
        ## 0 0  1  0 0 1 2
        ## 0 1  2  3 4 5
        visited = set()
        time = 0
        pos = 0
        visited.add(0)
        n = len(nextVisit)
        while len(visited) < n and time <6 :
            print(time,pos)
            if time % 2 == 0 :
                pos = nextVisit[pos]
                if time == 4:
                    print(time,pos)
            else:
                pos = (pos+1) % n
            time += 1
            visited.add(pos)
        return (time )%(10**9+7)
s= Solution713()
s.firstDayBeenInAllRooms([0,0,2])












