class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l + 1 < r:
            mid = (int(l + r) / 2)
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid
                else:
                    r = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid
                else:
                    r = mid
        if l == 0 and nums[l] != nums[l + 1]:
            return nums[l]
        if r == len(nums) - 1 and nums[r] != nums[r - 1]:
            return nums[r]
        if nums[l] != nums[l+1]  and  nums[l] != nums[l-1] :
            return nums[l]
        return nums[r]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l+1< r:
            mid = int((l+r)/2)
            if mid %2 == 0:
                if nums[mid] != nums[mid+1]:
                    r = mid
                else:
                    l =mid
            else:
                if nums[mid] != nums[mid-1]:
                    r= mid
                else:
                    l= mid
        if l == 0  and nums[l] != nums[l+1]:
            return nums[l]
        if nums[l] != nums[l-1] and nums[l] != nums[l+1]:
            return nums[l]
        return nums[r]


