##Given n non-negative integers a1, a2, ..., an ,
##where each represents a point at coordinate (i, ai).
##n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
##Find two lines, which together with x-axis forms a container,
##such that the container contains the most water.
##Note: You may not slant the container and n is at least 2.

##The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
##In this case, the max area of water (blue section) the container can contain is 49.
##Example:
##Input: [1,8,6,2,5,4,8,3,7]
##Output: 49


def maxArea2(height):
    if not height or len(height) < 2:
        return 0
    j = 0
    area = 0
    tmp1 = 0
    while j < len(height):
        if height[j] <= tmp1:
            j += 1
            continue
        i = j + 1
        while i < len(height):
            heighth = min(height[j], height[i])
            width = i - j
            area = max(area, heighth * width)
            i += 1
        tmp1 = height[j]
        j += 1
    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    maxarea = 0
    n = len(height)
    l = 0
    r = n - 1
    while l < r:
        maxarea = max((r - l) * min(height[l], height[r]),maxarea)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxarea
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))