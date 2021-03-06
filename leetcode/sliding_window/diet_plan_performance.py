##A dieter consumes calories[i] calories on the i-th day. 
##Given an integer k, for every consecutive sequence of k days
# (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k),
# they look at T, the total calories consumed during that sequence of k days
# (calories[i] + calories[i+1] + ... + calories[i+k-1]):
##If T < lower, they performed poorly on their diet and lose 1 point; 
##If T > upper, they performed well on their diet and gain 1 point;
##Otherwise, they performed normally and there is no change in points.
##Initially, the dieter has zero points.
# Return the total number of points the dieter has after dieting for calories.length days.
##Note that the total points can be negative.
##Example 1:
##Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
##Output: 0
##Explanation: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
##calories[0] and calories[1] are less than lower so 2 points are lost.
##calories[3] and calories[4] are greater than upper so 2 points are gained.
##Example 2:
# input: calories = [3,2], k = 2, lower = 0, upper = 1
##Output: 1
##Explanation: Since k = 2, we consider subarrays of length 2.
##calories[0] + calories[1] > upper so 1 point is gained.
##Example 3:
##Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
##Output: 0
##Explanation:
##calories[0] + calories[1] > upper so 1 point is gained.
##lower <= calories[1] + calories[2] <= upper so no change in points.
##calories[2] + calories[3] < lower so 1 point is lost.
##Constraints:
##1 <= k <= calories.length <= 10^5
##0 <= calories[i] <= 20000
##0 <= lower <= upper
def dietPlanPerformance(calories, k, lower, upper):
    l = 0
    res2 = 0
    total = 0
    if not calories or len(calories) == 0:
        return 0
    for r in range(len(calories)):
        total += calories[r]
 ##     if r-l+1 > l : 也可以
        while r - l + 1 > k:
            total -= calories[l]
            l += 1
        if r - l + 1 == k and total > upper:
            res2 += 1
        if r - l + 1 == k and total < lower:
            res2 -= 1
    return res2


print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))


class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        k_calories = 0
        score = 0
        for index, value in enumerate(calories):
            if index + 1 < k:
                k_calories += value
            else:
                if index + 1 == k:
                    k_calories += value
                else:
                    k_calories = k_calories - calories[index - k] + value
                if k_calories < lower:
                    score -= 1
                elif k_calories > upper:
                    score += 1
        return score
