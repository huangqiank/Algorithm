##Given two arrays, write a function to compute their intersection.
##Example 1:
##Input: nums1 = [1,2,2,1], nums2 = [2,2]
##Output: [2]
##Example 2:
##Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
##Output: [9,4]


def intersection(nums1, nums2):
    if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
        return []
    num1_set = set(nums1)
    num2_set = set(nums2)
    num_set = set()
    if len(num1_set) > len(num2_set):
        small_set = num2_set
        larget_set = num1_set
    else:
        small_set = num1_set
        larget_set = num2_set
    for i in small_set:
        if i in larget_set:
            num_set.add(i)
    return list(num_set)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
