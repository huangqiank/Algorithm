##You are given a circular array nums of positive and negative integers.
##If a number k at an index is positive, then move forward k steps. Conversely,
##if it's negative (-k), move backward k steps.
##Since the array is circular, you may assume that the last element's next element is the first element,
##and the first element's previous element is the last element.
##Determine if there is a loop (or a cycle) in nums.
# A cycle must start and end at the same index and the cycle's length > 1.
# Furthermore, movements in a cycle must all follow a single direction. In other words,
# a cycle must not consist of both forward and backward movements.
##Example 1:
##Input: [2,-1,1,2,2]
##Output: true
##Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is a3.
##Example 2:
##Input: [-1,2]
##Output: false
##Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle,
# because the cycle's length is 1. By definition the cycle's length must be greater than 1.
##Example 3:
##Input: [-2,1,-1,-2,-2]
##Output: false
##Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle,
# because movement from index 1 -> 2 is a forward movement,
# but movement from index 2 -> 1 is a backward movement.
# All movements in a cycle must follow a single direction.
##Note:
##-1000 ≤ nums[i] ≤ 1000
##nums[i] ≠ 0
##1 ≤ nums.length ≤ 5000
##Follow up:
##Could you solve it in O(n) time complexity and O(1) extra space complexity?
def circularArrayLoop(nums):
    index_set = set()
    n = len(nums)
    for i in range(len(nums)):
        if i in index_set:
            continue
        slow = i
        fast = i
        while True:
            index_set.add(i)
            slow = get_index(slow, nums[slow], n)
            new_index = get_index(fast, nums[fast], n)
            fast = get_index(new_index, nums[new_index], n)
            if fast == slow:
                if check(slow, n):
                    return True
                break
    return False


def check(slow, n):
    tmp = slow
    length = 0
    if nums[slow] == 0:
        flag = 0
    if nums[slow] > 0:
        flag = 1
    if nums[slow] < 0:
        flag = -1
    while True:
        if flag == 0 or nums[slow] == 0:
            return False
        if flag > 0 and nums[slow] < 0:
            return False
        if flag < 0 and nums[slow] > 0:
            return False
        slow = get_index(slow, nums[slow], n)
        length += 1
        if slow == tmp:
            break
    if length <= 1:
        return False
    return True


def get_index(index, num, n):
    if num >= 0:
        return (index + num) % n
    if num < 0:
        if index + num >= 0:
            return index + num
        return (index + num) % n


nums = [2,-1,1,2,2]
print(circularArrayLoop(nums))


def circularArrayLoop(self, nums):
    n = len(nums)
    visited = set()
    for i in range(n):
        if i not in visited:
            direction = nums[i]
            visited.add(i)
            numSet = set()
            numSet.add(i)
            j = (i + nums[i]) % n
            while j not in visited:
                visited.add(j)
                if nums[j] * direction < 0:
                    direction = nums[j]
                    numSet = set()
                    numSet.add(j)
                    j = (n + j + nums[j]) % n
                else:
                    numSet.add(j)
                    j = (n + j + nums[j]) % n
                if (n + j + nums[j]) % n == j:
                    numSet = set()
                elif j in numSet and len(numSet) >= 2:
                    return True
    return False
