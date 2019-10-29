def bfs_matrix2(a,k):
    row = len(a)-1
    col = len(a[0])-1
    i = 0    
    j = row
    while i <  j - 1:
        mid = int((i + j)/2)
        if a[mid][col]==k:
            return mid,col
        if a[mid][col] > k:
            j = mid
        if a[mid][col] < k:
            i = mid
    if a[i][col] >= k:
        cur_row = i
    else:
        cur_row = j
    c = 0
    b = col
    while c <= b:
        mid = int((c+b)/2)
        if a[cur_row][mid] == k:
            return cur_row,mid
        if a[cur_row][mid] > k:
            b = mid - 1
        if a[cur_row][mid] < k:
            c = mid + 1
    return False
d=[[1,2],[3,4]]
print(bfs_matrix2(d,4))

def matrix(a, b):
    row = len(a)
    col = len(a[0])
    left = 0
    right = row * col - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        cur_row = int(mid / col)
        cur_col = mid % col
        if a[cur_row][cur_col] == b:
            return cur_row,cur_col
        if a[cur_row][cur_col] > b:
            right = mid
        if a[cur_row][cur_col] < b:
            left = mid

    if a[int(left / col)][left % col] == b:
        return int(left / col),left % col

    if a[int(right / col)][right % col] == b:
        return int(right / col),right % col
    return False

d = [[1, 2], [3, 4]]
print(matrix(d, 5))

def bfs_near_num(a,k):
    row = len(a)
    col = len(a[0])
    i = 0
    j = row*col-1
    while i <= j:
        mid = int((i+j)/2)
        c = int(mid/col)
        b = mid%col
        if a[c][b] == k:
            return c,b
        if a[c][b] > k:
            j = mid-1
        if a[c][b] < k:
            i = mid + 1
    return False

def matrix(a,k):
    l=0
    row=len(a)
    col=len(a[0])
    r=col*row-1
    while l + 1 < r:
        mid=(l+r)/2
        if a[mid/col][mid%col] == k:
            return mid/col,mid%col
        if a[mid/col][mid%col] > k:
            r = mid
        if a[mid/col][mid%col] < k:
            l = mid
    if a[l/col][l%col]==k:
        return l/col,l%col
    if a[r/col][r%col]==k:
        return r/col,r%col
    return False
d=[[1,2],[3,4]]
print (bfs_near_num(d,3))



        
            