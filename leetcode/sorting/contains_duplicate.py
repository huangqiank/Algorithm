##Given an array of integers,
##find out whether there are two distinct indices i and j in the array
##such that the absolute difference between nums[i] and nums[j] is at most t
##and the absolute difference between i and j is at most k.
##Example 1:
##Input: nums = [1,2,3,1], k = 3, t = 0
##Output: true
##Example 2:
##Input: nums = [1,0,1,1], k = 1, t = 2
##Output: true
##Example 3:
##Input: nums = [1,5,9,1,5,9], k = 2, t = 3
##Output: false

########3是否存在
##给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
##使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
##并且 i 和 j 之间的差的绝对值最大为 ķ。
## 区分 // 和 int(/), 在有负数的情况下用//向下取整

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


def containsNearbyAlmostDuplicate2(nums, k, t):
    if k < 0 or t < 0:
        return False
    bucket_size = t + 1
    all_bucket = {}
    for i in range(len(nums)):
        index = nums[i] // bucket_size
        if index in all_bucket:
            return True
        if index - 1 in all_bucket and abs(nums[i] - all_bucket[index - 1]) < bucket_size:
            return True
        if index + 1 in all_bucket and abs(nums[i] - all_bucket[index + 1]) < bucket_size:
            return True
        all_bucket[index] = nums[i]
        if i >= k:
            del all_bucket[int(nums[i - k] // bucket_size)]
    return False

nums = [-3,3]
k = 2
t = 4
print(containsNearbyAlmostDuplicate2(nums, k, t))