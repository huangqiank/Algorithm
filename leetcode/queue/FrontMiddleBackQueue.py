####1670. Design Front Middle Back Queue
#Design a queue that supports push and pop operations in the front, middle, and back.
#Implement the FrontMiddleBack class:
#FrontMiddleBack() Initializes the queue.
#void pushFront(int val) Adds val to the front of the queue.
#void pushMiddle(int val) Adds val to the middle of the queue.
#void pushBack(int val) Adds val to the back of the queue.
#int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
#int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
#int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
#Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:
#Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
#Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
#Example 1:
#Input:
#["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
#[[], [1], [2], [3], [4], [], [], [], [], []]
#Output:
#[null, null, null, null, null, 1, 3, 4, 2, -1]
#Explanation:
#FrontMiddleBackQueue q = new FrontMiddleBackQueue();
##q.pushFront(1);   // [1]
#q.pushBack(2);    // [1, 2]
#q.pushMiddle(3);  // [1, 3, 2]
#q.pushMiddle(4);  // [1, 4, 3, 2]
#q.popFront();     // return 1 -> [4, 3, 2]
#q.popMiddle();    // return 3 -> [4, 2]
#q.popMiddle();    // return 4 -> [2]
#q.popBack();      // return 2 -> []
#q.popFront();     // return -1 -> [] (The queue is empty)


class Node:
    def __init__(self, val):
        self.pre = None
        self.next = None
        self.val = val

class FrontMiddleBackQueue:

    def __init__(self):
        self.head1 = Node(0)
        self.tail1 = Node(0)
        self.size1 = 0
        self.head2 = Node(0)
        self.tail2 = Node(0)
        self.size2 = 0
        self.head1.next = self.tail1
        self.tail1.pre = self.head1
        self.head2.next = self.tail2
        self.tail2.pre = self.head2

    def add(self, node1, node2):
        node2.next = node1.next
        node1.next.pre = node2
        node2.pre = node1
        node1.next = node2

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def pushFront(self, val: int) -> None:
        if self.size1 == self.size2:
            node = Node(val)
            self.add(self.head1, node)
            self.size1 += 1
        elif self.size1 > self.size2:
            node = Node(val)
            self.add(self.head1, node)
            node2 = self.tail1.pre
            self.remove(node2)
            self.add(self.head2, node2)
            self.size2 += 1

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.size1 == self.size2:
            self.add(self.tail1.pre, node)
            self.size1 += 1
        elif self.size1 > self.size2:
            node2 = self.tail1.pre
            self.remove(node2)
            self.add(self.tail1.pre, node)
            self.add(self.head2, node2)
            self.size2 += 1

    def pushBack(self, val: int) -> None:
        node = Node(val)
        if self.size1 == self.size2:
            self.add(self.tail2.pre, node)
            node2 = self.head2.next
            self.remove(node2)
            self.add(self.tail1.pre, node2)
            self.size1 += 1
        elif self.size1 > self.size2:
            self.add(self.tail2.pre, node)
            self.size2 += 1

    def popFront(self) -> int:
        if self.size1 == 0:
            return -1
        node = self.head1.next
        if self.size1 == self.size2:
            self.remove(node)
            node2 = self.head2.next
            self.remove(node2)
            self.add(self.tail1.pre, node2)
            self.size2 -= 1
        elif self.size1 > self.size2:
            self.remove(node)
            self.size1 -= 1
        return node.val

    def popMiddle(self) -> int:
        if self.size1 == 0:
            return -1
        node = self.tail1.pre
        if self.size1 == self.size2:
            node2 = self.head2.next
            self.remove(node)
            self.remove(node2)
            self.add(self.tail1.pre, node2)
            self.size2 -= 1
        elif self.size1 > self.size2:
            self.remove(node)
            self.size1 -= 1
        return node.val
    def popBack(self) -> int:
        if self.size1 == 0:
            return -1
        if self.size1 == self.size2:
            node = self.tail2.pre
            self.remove(node)
            self.size2 -= 1
        elif self.size1 > self.size2:
            node2 = self.tail1.pre
            self.remove(node2)
            self.add(self.head2, node2)
            node = self.tail2.pre
            self.remove(node)
            self.size1 -= 1
        return node.val








class Solution33:
    def maxTurbulenceSize(self, arr):
        if len(arr) <2:
            return len(arr)
        new =[]
        for i in range(0,len(arr)-1):
            if arr[i] < arr[i+1]:
                new.append(1)
            if arr[i] >arr[i+1]:
                new.append(-1)
            if arr[i] == arr[i+1]:
                new.append(0)
        print(new)
        dp = [0 for i  in range(len(new))]
        if new[0] == 0:
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1,len(new)):
            if new[i]*new[i-1] < 0:
                dp[i] =dp[i-1]+1
                continue
            if new[i] ==0:
                dp[i] = 0
                continue
            if new[i] ==-1 or new[i] ==1:
                dp[i] =1
                continue
        max_l = max(dp)+1
        return max_l
s = Solution33()
print(s.maxTurbulenceSize([37,199,60,296,257,248,115,31,273,176]))