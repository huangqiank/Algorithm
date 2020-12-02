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
            count += 1
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
intervals = [[10, 11], [4, 9], [4, 17], [11, 13], [14, 15]]
print(meeting_room2(intervals))


def meeting_room3(intervals):
    if not intervals or len(intervals) == 0:
        return 0
    res = []
    count = 0
    for i in range(len(intervals)):
        if len(res) == 0:
            res.append(intervals[i][1])
            count += 1

        last = res[0]
        if intervals[i][0] > last:
            heapq.heappush(res, intervals[i][1])
            count += 1
        else:
            heapq.heappop(res)
            heapq.heappush(res, intervals[i][1])
    return count


def h_index(citation):
    citation = sorted(citation, key=lambda index: index, reverse=True)
    l = 0
    r = len(citation) - 1
    while l + 1 < r:
        mid = int((l + r) / 2)
        if citation[mid] < mid + 1:
            r = mid
        else:
            l = mid
    if citation[r] >= r + 1:
        return r
    if citation[l] >= l + 1:
        return l


def contains_dulplicate(nums, k, t):
    if not nums or len(nums) == 0:
        return
    all_bucket = {}
    bucket_size = t + 1
    for i in range(len(nums)):
        index = nums[i] // bucket_size
        if index in all_bucket:
            return True
        if index - 1 in all_bucket and abs(all_bucket[index - 1] - nums[i]) < bucket_size:
            return True
        if index + 1 in all_bucket and abs(all_bucket[index + 1] - nums[i]) < bucket_size:
            return True
        all_bucket[index] = nums[i]
        if i >= k:
            del all_bucket[nums[i - k] / bucket_size]
    return False


def containsNearbyAlmostDuplicate(nums, k, t):
    if t < 0 or k < 0:
        return False
    allBuckets = {}
    bucketSize = t + 1
    for i in range(len(nums)):
        # m is bucket Index for nums[i]
        m = nums[i] / bucketSize
        # if there is a bucket already present corresponding to current number
        if m in allBuckets:
            return True
        # checking two adjacent buckets  m, m-1
        if (m - 1) in allBuckets and abs(nums[i] - allBuckets[m - 1]) < bucketSize:
            return True
        # checking two adjacent buckets m, m+1
        if (m + 1) in allBuckets and abs(nums[i] - allBuckets[m + 1]) < bucketSize:
            return True
        allBuckets[m] = nums[i]
        # removing the bucket corresponding to number out of our k sized window
        if i >= k:
            del allBuckets[nums[i - k] / bucketSize]
    return False


class node:
    def __init__(self, x):
        self.value = x
        self.next = None


def insertion_sort(head):
    if head is None:
        return
    root = node(0)
    root.next = head
    while head.next:
        if head.value <= head.next.value:
            head = head.next
        else:
            start = root
            tmp = head.next
            head.next = head.next.next
            while start.next:
                if start.next.value <= tmp.value:
                    start = start.next
            tmp.next = start.next
            start.next = tmp
    return root.next


def largest_num_deivide(nums):
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    left = largest_num_deivide(nums[:n // 2], n // 2)
    right = largest_num_deivide(nums[n // 2:], n - n // 2)
    return largest_num_merge(left, right, n // 2, n - n // 2)


def largest_num_merge(left, right, i, j):
    res = []
    index1 = 0
    index2 = 0
    while index1 < i and index2 < j:
        a = left[0]
        b = right[0]
        c = str(a) + str(b)
        d = str(b) + str(a)
        if int(c) < int(d):
            res.append(b)
            index2 += 1
            right.pop(0)
        else:
            res.append(a)
            index1 += 1
            left.pop(0)
    while index1 < i:
        res.append(left[0])
        left.pop(0)
        index1 += 1
    while index2 < i:
        res.append(right[0])
        right.pop(0)
        index2 += 1

    return res


def intersect(a, b):
    if a[1] < b[0]:
        return 0
    return 1


def merge(a, b):
    return [a[0], max(a[1], b[1])]


def merge_intervals(nums):
    if nums is None:
        return None
    if len(nums) == 1:
        return nums[1]
    if len(nums) == 0:
        return
    nums = sorted(nums, key=lambda num: (num[0], num[1]))
    res = []
    res.append(nums[0])
    for i in range(1, len(nums), 1):
        last = res[-1]
        if intersect(last, nums[i]) == 0:
            res.append(nums[i])
        if intersect(last, nums[i]) == 1:
            res.pop()
            res.append([last[0], max(last[1], nums[i][1])])
    return res


def sortList(self, head):
    if head == None:
        return None
    length = 0
    tmp = head
    while tmp:
        tmp = tmp.next
        length += 1
    return self.sort(head, length)


def sort(self, head, length):
    if length == 1:
        return head
    head2 = head
    for i in range(int(length / 2)):
        head2 = head2.next
    left = self.sort(head, int(length / 2))
    right = self.sort(head2, length - int(length / 2))
    return self.merge(left, right, int(length / 2), length - int(length / 2))


def merge(self, left, right, length1, length2):
    dummy = ListNode(0)
    head = dummy
    pointer1 = 0
    pointer2 = 0
    while pointer1 < length1 and pointer2 < length2:
        if left.val < right.val:
            head.next = left
            left = left.next
            pointer1 += 1
            head = head.next
        else:
            head.next = right
            right = right.next
            pointer2 += 1
            head = head.next
    while pointer1 < length1:
        pointer1 += 1
        head.next = left
        left = left.next
        head = head.next
    while pointer2 < length2:
        pointer2 += 1
        head.next = right
        right = right.next
        head = head.next
    head.next = None
    return dummy.next


def sort_list(head):
    if head is None:
        return None
    length = 0
    tmp = head
    while tmp:
        tmp = tmp.next
        length += 1
    return divide(head, length)


def divide(head, length):
    if length == 1:
        return head
    n = length // 2
    tmp1 = head
    tmp2 = head
    i = 0
    while i < n:
        tmp2 = tmp2.next
        i += 1
    left = divide(tmp1, n)
    right = divide(tmp2, length - n)
    return merge1(tmp1, tmp2, left, right)


def merge1(tmp1, tmp2, left, right):
    new_head = node(0)
    start = new_head
    i = 0
    j = 0
    while i < left and j < right:
        if tmp1.value < tmp2.value:
            start.next = tmp1
            tmp1 = tmp1.next
            i += 1
            start = start.next
        else:
            start.next = tmp2
            tmp2 = tmp2.next
            j += 1
            start = start.next
    while i < left:
        start.next = tmp1
        tmp1 = tmp1.next
        i += 1
        start = start.next
    while j < right:
        start.next = tmp2
        tmp2 = tmp2.next
        j += 1
        start = start.next
    start.next = None
    return new_head.next


def sort_color(nums):
    if not nums:
        return
    p = 0
    q = len(nums) - 1
    sort_color_help(nums, p, q)
    return nums


def sort_color_help(nums, p, q):
    if p < q:
        d = partition_help(nums, p, q)
        sort_color_help(nums, p, d - 1)
        sort_color_help(nums, d + 1, q)


def partition_help(nums, p, q):
    j = p - 1
    for i in range(p, q):
        if nums[i] < nums[q]:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    j += 1
    nums[j], nums[q] = nums[q], nums[j]
    return j

print(sort_color([2,0,2,1,1,0]))
