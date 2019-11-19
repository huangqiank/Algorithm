##Given an array nums containing n + 1 integers
##where each integer is between 1 and n (inclusive),
##prove that at least one duplicate number must exist.
##Assume that there is only one duplicate number,
##find the duplicate one.

##Example 1:

##Input: [1,3,4,2,2]
##Output: 2
##Example 2:
##Input: [3,1,3,4,2]
##Output: 3
##Note:

##You must not modify the array (assume the array is read only).
##You must use only constant, O(1) extra space.
##Your runtime complexity should be less than O(n2).
##There is only one duplicate number in the array,
##but it could be repeated more than once.

##            -
##        -       -
## -------         -
##        -       -
##            -
##slow ,fast 第一次走相遇的时候 slow 走了n 步 ，n是圆周长的倍数
##链表起点到圆的起点距离是m 则 slow 在圆内走了  n-m 步
##现在在来一个新指针走 m步，他们一定相遇

##双指针
def findDuplicate(nums):
    if not nums:
        return
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    new = 0
    while True:
        slow = nums[slow]
        new = nums[new]
        if slow == new:
            return new



##二分查找
def findDuplicate2(nums):
    n = len(nums)
    l = 1
    r = n
    while l + 1 < r:
        mid = int((l + r) / 2)
        j = 0
        for i in nums:
            if i <= mid:
                j += 1
        if j > mid:
            r = mid
        if j <= mid:
            l = mid
    j = 0
    for i in nums:
        if i == l:
            j += 1
    if j >= 2:
        return l
    j = 0
    for i in nums:
        if i == r:
            j += 1
    if j >= 2:
        return r
nums = [2,2,2,2,2]
print(findDuplicate2(nums))
