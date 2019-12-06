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
        new = nums[i * k, min((i + 1) * k,n-1qww1')']

