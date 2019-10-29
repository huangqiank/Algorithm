# _*_coding:utf-8_*_
#### [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#### O(log n)
## pivot，满足同时小于左右或者大于左右。
##二分查找中间点，若等于返回
##不等于判断pivot，不是则正常
##  mid <= right : 二段
##  mid > right : 一段
##class Solution:
#   def search(self, nums: List[int], target: int) -> int:

class Solution:
    def search(self, nums, target):
        if nums is None or len(nums)==0 or target is None :
            return -1
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                if nums[mid] <= nums[-1] and target > nums[-1]:  ## mid is in second
                    right = mid
                if nums[mid] <= nums[-1] and target <= nums[-1]:  ## mid is in second
                    left = mid
                if nums[mid] > nums[-1]:  ## mid is in first
                    left = mid
            if target < nums[mid]:
                if nums[mid] <= nums[-1]:
                    right = mid
                if nums[mid] > nums[-1] and target > nums[-1]:  ## b在一段，mid在一段
                    right = mid
                if nums[mid] > nums[-1] and target <= nums[-1]:  ##mid在first，b在二段
                    left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1






nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
### 4 和没有的时候出现targetug



# _*_coding:utf-8_*_
#### [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#### O(log n)
## pivot，满足同时小于左右或者大于左右。
##二分查找中间点，若等于返回
##不等于判断pivot，不是则正常
##pivot则左查找或者右边查找
##右小左大
def search_rotated_sorted_array(a, b):
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        print("left " + str(left))
        print("right " + str(right))
        print("mid " + str(mid))
        if a[mid] == b:
            return mid
        if b > a[mid] and b < a[right]:
            left = mid
        else:
            print("left " + str(a[left]))
            print("right " + str(a[right]))
            print("mid " + str(a[mid]))
            right = mid
    if a[left] == b:
        return left
    if a[right] == b:
        return right
    return -1


## pivot 永远在中间数左边中间数小于左边且小于右边第二组，中间数大于左边且大于右边第一组
## b > mid. 若b小于右边，则在mid -----右边之间，在第二段
## b < mid, 若b小于左边, 则在左边 ---- mid之间，在第二段

## b > mid, 若b大于右边，则在左边 ---mid之间，在第一段
## b < mid, 若b大于左边, 则在左边 ---mid之间，在第一段

##print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 7))
print(search_rotated_sorted_array([10, 11, 5, 6, 7, 8, 9], 5))
##print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3))yu
