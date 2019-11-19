##Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
##Note:
##The number of elements initialized in nums1 and nums2 are m and n respectively.
##You may assume that nums1 has enough space
# (size that is greater or equal to m + n) to hold additional elements from nums2.
##Example:
##Input:
##nums1 = [1,2,3,0,0,0], m = 3
##nums2 = [2,5,6],       n = 3
##Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    nums1_copy = nums1[:m]
    k = 0
    while i < m and j < n:
        if nums1_copy[i] <= nums2[j]:
            nums1[k] = nums1_copy[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1
    if i < m:
        nums1[k:m + n] = nums1_copy[i:m]
    if j < n:
        nums1[k:m + n] = nums2[j:n]
    return nums1
print(merge([1],1,[],0))