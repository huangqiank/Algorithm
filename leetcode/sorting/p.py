########是否存在#######
##给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
##使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
##并且 i 和 j 之间的差的绝对值最大为 ķ。
## 区分 // 和 int(/), 在有负数的情况下用//向下取整
def containsNearbyAlmostDuplicate(nums, k, t):
    if not nums or len(nums) == 0:
        return False
    if t < 0:
        return False
    n = len(nums)
    num_partition = int(n / k)
    for i in range(num_partition):
        new = nums[i * k, min((i + 1) * k, n - 1)]


class node():
    def __init__(self, x):
        self.next = None
        self.value = x


def insertion_sort_list(head):
    root = node(0)
    root.next = head
    while head.next:
        if head.val <= head.next.val:
            head = head.next
        else:
            tmp = head.next
            start = root
            while start.next and start.next.value < tmp.value:
                start = start.next
            tmp.next = start.next
            start.next = tmp
    return root.next


def largest_number(nums):
    if not nums:
        return
    for i in nums:
        if i != 0:
            return "".join(merge_sort(nums, len(nums)))
    return "0"


def merge_sort(nums, n):
    if n == 1 :
        return [str(nums[0])]
    left = merge_sort(nums[:int(n / 2)], int(n / 2))
    right = merge_sort(nums[int(n / 2):], n - int(n / 2))
    return merge(left, right, int(n / 2), n - int(n / 2))


def merge(left, right, left_length, right_length):
    res = []
    p = 0
    q = 0
    while p < left_length and q < right_length:
        a = str(left[p]) + str(right[q])
        b = str(right[q]) + str(left[p])
        if a > b:
            res.append(left[p])
            p += 1
        else:
            res.append(right[q])
            q += 1
    if p < left_length:
        res.extend(left[p:])
    if q < right_length:
        res.extend(right[q:])
    return res

print(5//2)
print(int(5/2))
a = [0,30,90,1000,2]
print(largest_number(a))

