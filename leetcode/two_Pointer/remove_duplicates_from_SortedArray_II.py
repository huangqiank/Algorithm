##Given a sorted array nums,
##remove the duplicates in-place
##such that duplicates appeared at most twice
##and return the new length.

##Do not allocate extra space for another array,
##you must do this by modifying the input array in-place with O(1)
##extra memory.

##Example 1:
##Given nums = [1,1,1,2,2,3],
##Your function should return length = 5,
##with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

##It doesn't matter what you leave beyond the returned length.
##Example 2:
##Given nums = [0,0,1,1,1,1,2,3,3],
##Your function should return length = 7,
##with the first seven elements of nums being modified to
##0, 0, 1, 1, 2, 3 and 3 respectively.

##It doesn't matter what values are set beyond the returned length.
##Clarification:
##Confused why the returned value is an integer but your answer is an array?

def removeDuplicates(nums):
    if not nums:
        return 0
    if len(nums) < 3:
        return len(nums)
    j = 0
    i = 0
    while i < len(nums):
        tmp = nums[i]
        if j >= 2 and tmp == nums[j - 1] and tmp == nums[j - 2]:
            k = i
            while k < len(nums) and nums[k] == tmp:
                k += 1
            i = k
        if i < len(nums):
            nums[j] = nums[i]
            j += 1
            i += 1
    print(j)
    return nums


nums = [1, 1, 1]
print(removeDuplicates(nums))


def removeDuplicates(nums, k):
    i = 0
    for n in nums:
        if i < k or n != nums[i - k]:
            nums[i] = n
            i += 1
    return i
