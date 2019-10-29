##Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
##Integers in each row are sorted from left to right.
##The first integer of each row is greater than the last integer of the previous row.
##class Solution:
##def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
##Example 1:
##Input:
##matrix = [
##  [1,   3,  5,  7],
##  [10, 11, 16, 20],
##  [23, 30, 34, 50]
##]
##target = 3
##Output: true
##Example 2:

##Input:
##matrix = [
##  [1,   3,  5,  7],
##  [10, 11, 16, 20],
##  [23, 30, 34, 50]
##]
##target = 13
##Output: false
class Solution:
    def searchMatrix(self, matrix, target):
        left = 0
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        right = len(matrix) * len(matrix[0])
        row = len(matrix[0])
        while left + 1 < right:
            mid = int((left + right) / 2)
            row_num = int(mid / row)
            col_num = mid % row
            if matrix[row_num][col_num] == target:
                return True
            if matrix[row_num][col_num] > target:
                right = mid
            if matrix[row_num][col_num] < target:
                left = mid
        if matrix[int(left / row)][left % row] == target:
            return True
        if matrix[int(right / row)][right % row] == target:
            return True
        return False


def searchMatrix(matrix, target):
    left = 0
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    right = len(matrix) * len(matrix[0])-1
    row = len(matrix[0])
    while left + 1 < right:
        mid = int((left + right) / 2)
        row_num = int(mid / row)
        col_num = mid % row
        if matrix[row_num][col_num] == target:
            return True
        if matrix[row_num][col_num] > target:
            right = mid
        if matrix[row_num][col_num] < target:
            left = mid
    if matrix[int(left / row)][left % row] == target:
        return True
    if matrix[int(right / row)][right % row] == target:
        return True
    return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 50

print(searchMatrix(matrix,50))