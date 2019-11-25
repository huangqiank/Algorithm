##Given two arrays, write a function to compute their intersection.
##Example 1:
##Input: nums1 = [1,2,2,1], nums2 = [2,2]
##Output: [2,2]
##Example 2:
##Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
##Output: [4,9]
##Note:
##Each element in the result should appear as many times as it shows in both arrays.
##The result can be in any order.
##Follow up:
##What if the given array is already sorted?
##How would you optimize your algorithm?
##What if nums1's size is small compared to nums2's size?
##Which algorithm is better?
##What if elements of nums2 are stored on disk,
##and the memory is limited such that you cannot load all elements into the memory at once?
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
        return []
    num_set = []
    if len(nums1) > len(nums2):
        small_list = nums2
        larget_list = nums1
    else:
        small_list = nums1
        larget_list = nums2
    j = 0
    i = 0
    while i < len(small_list) and j < len(larget_list):
        if small_list[i] == larget_list[j]:
            num_set.append(small_list[i])
            i += 1
            j += 1
        elif small_list[i] < larget_list[j]:
            i += 1
        else:
            j += 1
    return num_set


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
