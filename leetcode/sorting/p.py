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
    if n == 1:
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


def meeting_room(intervals):
    intervals = sorted(intervals, key=lambda key: (key[0], key[1]))
    for i in range(len(intervals) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            return False
    return True


def sort_linked_list(head):
    if head is None:
        return None
    tmp = head
    n = 0
    while tmp:
        tmp = tmp.next
        n += 1
    sort_linked_list_help(head, n)


def sort_linked_list_help(head, n):
    if n == 1:
        return head
    head2 = head
    for i in range(int(n / 2)):
        head2 = head2.next
    left = sort_linked_list_help(head, int(n / 2))
    right = sort_linked_list_help(head2, n - int(n / 2))
    return merge_help(left, right, int(n / 2), n - int(n / 2))


def merge_help(head, head2, n1, n2):
    new = node(0)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if head.value < head2.value:
            new.next = head
            head = head.next
            new.next = head
            i += 1
        else:
            new.next = head2
            head2 = head2.next
            new.next = head
            j += 1
    while i < n1:
        new.next = head
        head = head.next
        new.next = head
        i += 1
    while j < n2:
        new.next = head
        head = head.next
        new.next = head
        j += 1
    return new.next


def intersect(a, b):
    ## 包含
    if a[1] >= b[1]:
        return 0
    ## 相交
    if a[1] >= b[0]:
        return 1
    ##
    if a[1] < b[0]:
        return -1


def merge_interval(input):
    input = sorted(input, key=lambda k: (k[0], k[1]))
    res = []
    res.append(input[0])
    for i in range(1, len(input), 1):
        last = input[-1]
        if 0 == intersect(last, input[i]):
            continue
        if 1 == intersect(last, input[i]):
            res.pop()
            res.append([last[0], input[i][1]])
        if -1 == intersect(last, input[i]):
            res.append(input[i])
    return res


def sort_color(nums):
    if not nums:
        return nums
    p = 0
    sort_color_help(nums, p, len(nums))
    return nums


def sort_color_help(nums, p, q):
    if p < q:
        partition = partition_help(nums, p, q)
        sort_color_help(nums, p, partition - 1)
        sort_color_help(nums, partition + 1, q)


def partition_help(nums, p, q):
    j = p - 1
    for i in range(p, q):
        if nums[i] < nums[q]:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    j += 1
    nums[j], nums[q] = nums[q], nums[j]
    return j


##  相交    b[0]<a[1] < b[1]
##  包含    b[0]<b[1]<a[1]
##  不想交  a[1]< b[0]<b[1]
import heapq


def meeting_room2(intervals):
    if not intervals or len(intervals) == 0:
        return 0
    res = []
    count = 0
    for i in range(len(intervals)):
        if len(res) == 0:
            res.append(intervals[i][1])
            count+=1
            continue
        last = res[0]
        if last < intervals[i][0]:
            count += 1
            heapq.heappush(res, intervals[i][1])
        else:
            heapq.heappop(res)
            heapq.heappush(res, intervals[i][1])
    return count


intervals = [[13, 15], [1, 13]]
print(meeting_room2(intervals))
intervals = [[10, 11], [4, 9], [4, 17],[11,13],[14,15]]
print(meeting_room2(intervals))

