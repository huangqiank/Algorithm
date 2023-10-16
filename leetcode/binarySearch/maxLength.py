##1891. Cutting Ribbons
#You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.
#For example, if you have a ribbon of length 4, you can:
#Keep the ribbon of length 4,
#Cut it into one ribbon of length 3 and one ribbon of length 1,
#Cut it into two ribbons of length 2,
#Cut it into one ribbon of length 2 and two ribbons of length 1, or
#Cut it into four ribbons of length 1.
#Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.
#Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you

# cannot obtain k ribbons of the same length.

class Solution:
    def maxLength(self, ribbons, k: int):
        right = int(sum(ribbons) / k)

        print(right)
        while left + 1 < right:
            mid = int((left + right) / 2)
            count = 0
            for i in range(len(ribbons)):
                count += int(ribbons[i] / mid)
            if count >= k:
                left = mid
            else:
                right = mid
        count = 0
        if right == 0:
            return 0
        for i in range(len(ribbons)):
            count += int(ribbons[i] / right)
        if count >= k:
            return right
        return left


ribbons = [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,1,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000]
k =49
s=Solution()
print(s.maxLength(ribbons,k))