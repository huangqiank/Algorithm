##Write an efficient algorithm that searches for a value in an m x n matrix.
##This matrix has the following properties:
##Integers in each row are sorted in ascending from left to right.
##Integers in each column are sorted in ascending from top to bottom.
##Example:
##Consider the following matrix:
##[
##  [1,   4,  7, 11, 15],
##  [2,   5,  8, 12, 19],
##  [3,   6,  9, 16, 22],
##  [10, 13, 14, 17, 24],
##  [18, 21, 23, 26, 30]
##]
##Given target = 5, return true.
##Given target = 20, return false.
##行小于target的几行
##列小于target的几列

##[row][col]

def searchMatrix(matrix, target):
    if not matrix:
        return False
    row_num = len(matrix)
    col_num = len(matrix[0])
    l = row_num - 1
    m = 0
    while l >= 0 and m < col_num:
        if matrix[l][m] == target:
            return True
        if matrix[l][m] < target:
            m += 1
        else:
            l -= 1
    return False


matrix = [[-5]]
print(searchMatrix(matrix, -5))
