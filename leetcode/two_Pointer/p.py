def three_sum_smaller(nums, k):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] + nums[i] == k:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1

            if nums[l] + nums[r] + nums[i] < k:
                count += r - l
                l += 1
            else:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
    return count


def three_sum(nums):
    nums = sorted(nums)
    res = []
    if not nums or len(nums) < 3:
        return res
    for i in range(len(nums)):
        if nums[i] > 0:
            return res
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([i, l, r])
                tmp = nums[l]
                while nums[l] == tmp and l < r:
                    l += 1
                tmp = nums[r]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue
            if nums[i] + nums[l] + nums[r] < 0:
                tmp = nums[l]
                while l < r and tmp == nums[l]:
                    l += 1
                continue
            if nums[i] + nums[l] + nums[r] > 0:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
                continue
    return res


def three_sum_smaller(nums, target):
    nums = sorted(nums)
    res = []
    count = 0
    if not nums or len(nums) < 3:
        return res
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] < target:
                count = count + r - l
                l += 1
                continue
            if nums[i] + nums[l] + nums[r] >= target:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
                continue
    return count


def three_sum_closed(nums, target):
    nums = sorted(nums)
    res = []
    dif = float("inf")
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == target:
                return [i, l, r]
            if abs(nums[i] + nums[l] + nums[r] - target) < dif:
                res = [i, l, r]
            if nums[i] + nums[l] + nums[r] < target:
                tmp = nums[l]
                while l < r and tmp == nums[l]:
                    l += 1
                continue
            if nums[i] + nums[l] + nums[r] > target:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
                continue
    return res


def threeSumClosest(nums, target):
    dif = float('inf')
    nums = sorted(nums)
    n = len(nums)
    res = []
    if not nums or len(nums) < 3:
        return res
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return [nums[i], nums[l], nums[r]]
            if total < target:
                tmp = nums[l]
                if abs(target - total) < dif:
                    dif = abs(target - total)
                    res = [nums[i], nums[l], nums[r]]
                while nums[l] == tmp and l < r:
                    l += 1
                continue
            if total > target:
                tmp = nums[r]
                if abs(target - total) < dif:
                    dif = abs(target - total)
                    res = [nums[i], nums[l], nums[r]]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue
    return res


## n -1 , n-2, n-3
def four_sum_target(nums, target):
    res = []
    if not nums or len(nums) < 4:
        return
    nums = sorted(nums)
    n = len(nums)
    for i in range(0, n - 3):
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            total = nums[i] + nums[j]
            l = j + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] + total == target:
                    res.append((i, j, l, r))
                    tmp = nums[l]
                    while l < r and tmp == nums[l]:
                        l += 1
                    tmp = nums[r]
                    while l < r and tmp == nums[r]:
                        r -= 1
                    continue
                if nums[l] + nums[r] + total < target:
                    tmp = nums[l]
                    while l < r and tmp == nums[l]:
                        l += 1
                else:
                    tmp = nums[r]
                    while l < r and tmp == nums[r]:
                        r -= 1
    return res


def four_sum(nums, target):
    res = []
    if not nums or len(nums) < 4:
        return res
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 3):
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue
            if j - i > 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = n - 1
            total = nums[i] + nums[j]
            while l < r:
                if total + nums[l] + nums[r] == target:
                    print(l)
                    print(r)
                    print("\n")
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
    return res


##n-4,n-3,n-2,n-1
def four_sum(nums, target):
    if not nums or len(nums) < 4:
        return
    res = []
    n = len(nums)
    for i in range(0, n - 3):
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] == target:
                    res.append((nums[i], nums[j], nums[l], nums[r]))
                    tmp1 = nums[l]
                    while tmp1 == nums[l] and l < r:
                        l += 1
                    tmp2 = nums[r]
                    while l < r and tmp2 == nums[r]:
                        r -= 1
                    continue
                if nums[i] + nums[j] + nums[l] + nums[r] < target:
                    tmp1 = nums[l]
                    while tmp1 == nums[l] and l < r:
                        l += 1
                    continue
                if nums[i] + nums[j] + nums[l] + nums[r] > target:
                    tmp1 = nums[r]
                    while tmp1 == nums[r] and l < r:
                        r -= 1
                    continue
    return res


def merge_sorted_array(nums1, m, nums2, n):
    nums_copy = nums1[:m]
    i = 0
    j = 0
    k = 0
    while i < m and j < n:
        if nums_copy[i] <= nums2[j]:
            nums1[k] = nums_copy[i]
            i += 1
            k += 1
        else:
            nums1[k] = nums2[j]
            j += 1
            k += 1
    if i < m:
        nums1[k:m + n] = nums1[i:m]
    if j < n:
        nums1[k:m + n] = nums2[j:n]
    return nums1


def implement_str(haystack, needle):
    i = 0
    m = len(haystack)
    n = len(needle)
    while i < m - n + 1:
        if haystack[i:i + n] == needle:
            return i
        i += 1
    return -1


def linked_list_cycle(head):
    slow = head
    fast = head
    if not head:
        return False
    while fast != None and fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def linked_list_cycle(head):
    slow = head
    fast = head
    if not head:
        return False
    while fast != None and fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    new = head
    while slow and slow.next:
        new = new.next
        slow = slow.next
        if slow == new:
            return slow
    return -1


def backspace_compare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    m = 0
    n = 0
    while i >= 0 and j >= 0:
        while i >= 0 and (s[i] == "#" or m > 0):
            if s[i] == "#":
                m += 1
            else:
                m -= 1
            i -= 1
        while j >= 0 and (t[j] == "#" or n > 0):
            if t[i] == "#":
                n += 1
            else:
                n -= 1
            j -= 1
        if i < 0 or j < 0:
            break
        if s[i] != t[j]:
            return False
        i -= 1
        j -= 1
    while i >= 0 and (s[i] == "#" or m > 0):
        if s[i] == "#":
            m += 1
        else:
            m -= 1
        i -= 1
    if i >= 0 and s[i] != "#":
        return False
    while j >= 0 and (t[j] == "#" or n > 0):
        if t[i] == "#":
            n += 1
        else:
            n -= 1
        j -= 1
    if j >= 0 and t[j] != "#":
        return False
    return True


def max_area(heights):
    area = 0
    tmp = 0
    i = 0
    if heights is None or len(heights) < 2:
        return -1
    while i < len(heights):
        if heights[i] <= tmp:
            i += 1
            continue
        j = i + 1
        while j < len(height):
            height = max(heights[i], heights[j])
            width = j - i
            area = max(area, width * height)
            j += 1
        tmp = heights[i]
        i += 1
    return area


def implement_str(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if n < m:
        return -1
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1


def move_zero(nums):
    n = len(nums)
    i = 0
    j = 0
    while i < n:
        if nums[i] == 0:
            i += 1
        else:
            nums[j] = nums[i]
            i += 1
            j += 1
    for t in range(j, len(nums)):
        nums[t] = 0
    return nums


def k_diff_pairs_in_an_array(nums, k):
    if not nums:
        return
    nums = sorted(nums)
    n = len(nums)
    count = 0
    for i in range(0, n, 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        while j < n:
            if nums[j] - nums[i] == k:
                count += 1
                break
            if nums[j] - nums[i] < k:
                j += 1
            if nums[j] - nums[i] > k:
                break
    return count


def find(s, d):
    d = sorted(d, key=lambda x: (-len(d), x))
    for word in d:
        if check(s, word):
            return word
    return -1


def check(s, word):
    j = 0
    for i in range(len(word)):
        k = s.find(word[i], j)
        if k == -1:
            return False
        j = k + 1
    return True


def max_consecutive_one(nums):
    if not nums or len(nums) == 0:
        return 0
    left = 0
    right = 0
    nums_dict = {0: 0, 1: 0}
    max_length = 0
    n = len(nums)
    if len(nums) == 1:
        return 1
    while right < n:
        nums_dict[nums[right]] += 1
        right += 1
        if nums_dict[0] >= 1:
            while nums_dict[0] > 0:
                nums_dict[nums[left]] -= 1
                left += 1
        max_length = max(max_length, right - left)
    return max_length


#   r
# [0,0,0,0,1]


def length_longest_substring_two_distinct(nums):
    left = 0
    right = 0
    max_length = 0
    nums_dict = {}
    n = len(nums)
    if n < 3:
        return n
    while right < n:
        if nums[right] not in nums_dict:
            nums_dict[nums[right]] = 1
        else:
            nums_dict[nums[right]] += 1
        right += 1
        while len(nums_dict) >= 3:
            nums_dict[nums[left]] -= 1
            if nums_dict[nums[left]] == 0:
                del nums_dict[nums[left]]
            left += 1
        max_length = max(max_length, right - left)
    return max_length


def palindrome_num(num):
    num = str(num)
    x = ''
    for i in range(len(num) - 1, -1, -1):
        x += num[i]
    return x == num


def k_diff_pairs_in_an_array(nums, k):
    if not nums or len(nums) < 2:
        return -1
    nums = sorted(nums)
    n = len(nums)
    count = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        while j < n:
            if nums[j] - nums[i] == k:
                j += 1
                count += 1
                continue
            if nums[j] - nums[i] > k:
                break
            if nums[j] - nums[i] < k:
                j += 1
                continue
    return count


def max_consecutive_ones(nums):
    left = 0
    right = 0
    n = len(nums)
    nums_dict = {0: 0, 1: 0}
    length = 0
    while right < n:
        nums_dict[nums[right]] += 1
        right += 1
        if nums_dict[0] > 0:
            while nums_dict[0] > 0:
                nums_dict[nums[left]] -= 1
                left += 1
            length = max(length, right - left)
    return length


def length_longest_two_distinct_nums(nums):
    max_length = 0
    left = 0
    right = 0
    nums_dict = {}
    n = len(nums)
    while right < n:
        if nums[right] not in nums_dict:
            nums_dict[nums[right]] = 1
        else:
            nums_dict[nums[right]] += 1
        right += 1
        if len(nums_dict) > 2:
            while len(nums_dict) > 2:
                nums_dict[nums[left]] -= 1
                if nums_dict[nums[left]] == 0:
                    del nums_dict[nums[left]]
                left += 1
            max_length = max(max_length, right - left)
    return nums_dict


def palindrome_linked_list(head):
    slow = head
    fast = head
    pre = None
    mid = None
    while fast and fast.next:
        mid = slow
        slow = slow.next
        fast = fast.next.next
        mid.next = pre
        pre = mid
    if fast != None:
        slow = slow.next
    while slow and pre:
        if slow.value != mid.value:
            return False
        slow = slow.next
        mid = mid.next
    return True


def partition(head, x):
    if not head:
        return
    small = node(0)
    large = node(2)
    tmp1 = small
    tmp2 = large
    while head:
        if head.value < x:
            tmp1.next = head
            tmp1 = tmp1.next
        else:
            tmp2.next = head
            tmp2 = tmp2.next
        head = head.next
    tmp1.next = large.next
    return small.next


def palindrom_num(x):
    x = str(x)
    y = ""
    for i in range(len(x) - 1, -1, -1):
        y += x[i]
    return x == y


def longest_word_in_dictionary(s, d):
    d = sorted(d, key=lambda x: (-len(x), x))
    for word in d:
        if check(s, word):
            return word
    return


def check(s, word):
    j = 0
    for i in range(len(word)):
        k = s.find(word[i], j)
        if k == -1:
            return -1
        j = k + 1
    return 1


def max_consecutive_one2(nums):
    if not nums or len(nums) == 0:
        return
    nums_dict = {0: 0, 1: 0}
    left = 0
    right = 0
    max_length = 0
    while right < len(nums):
        nums_dict[nums[right]] += 1
        right += 1
        while nums_dict[0] > 1:
            nums_dict[nums[left]] -= 1
            left += 1
        max_length = max(max_length, right - left)
    return max_length


def reverse_str(s):
    i = 0
    j = len(s) - 1
    mid = int(len(s) / 2)
    t = 0
    while t < mid:
        s[i], s[j] = s[j], s[i]
        i += 1
        j += 1
        t += 1
    return s


def remove_element(nums, a)
    i = 0
    j = 0
    n = len(nums)
    while j < n:
        if nums[j] == a:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    return i


def reverse_vowels_of_a_str(s):
    s = [s[i] for i in range(len(s))]
    vowel_set = set()
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowel_list:
        vowel_set.add(vowel)
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and s[i] not in vowel_set:
            i += 1
        while i < j and s[j] not in vowel_set:
            j -= 1
        if i < j and s[i] in vowel_set and s[j] in vowel_set:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return s


##
# 1->2->3->4


def remove_nth_node(head, n):
    slow = node(0)
    fast = node(0)
    slow.next = head
    fast.next = head
    i = 0
    j = 0
    while fast.next != None:
        if j < n:
            fast = fast.next
            j += 1
        else:
            i += 1
            slow = slow.next
            fast = fast.next
    slow.next = slow.next.next
    if i == 0:
        return head.next
    return head


def is_palindrome(s):
    s = filter(str.isalnum, s)
    s = ''.join(list(s))
    s = s.lower()
    i = 0
    j = len(s) - 1
    n = len(s) - 1
    while i <= n and j >= 0:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    if j != 0 or i != n:
        return False
    return True


def subarray_product_less_than_k(nums, k):
    left = 0
    prod = 1
    ans = 0
    if k <= 1:
        return 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans


def length_two_distinct_characters(s):
    if not s:
        return
    s_dict = {}
    left = 0
    right = 0
    max_length = 0
    while right < len(s):
        s_dict[s[right]] += 1
        while len(s_dict) >= 3:
            s_dict[s[left]] -= 1
            if s_dict[s[left]] == 0:
                del s_dict[s[left]]
            left += 1
        max_length = max(max_length, right - left)
        right += 1
    return max_length


def remove_duplicated_from_sorted_array(nums):
    i = 0
    j = 0
    if not nums or len(nums) < 3:
        return nums
    while i < len(nums):
        tmp = nums[i]
        if j >= 2 and tmp == nums[j-1] and tmp == nums[j - 2]:
            k = i
            while k < len(nums) and nums[k] == tmp:
                k += 1
            i = k
        if j < len(nums):
            nums[j] = nums[i]
            i += 1
            j += 1
    return j


