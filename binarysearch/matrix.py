def bfs_matrix2(a,k):
    row = len(a)-1
    col = len(a[0])-1
    i = 0    
    j = row
    while i <  j - 1:
        mid = (i + j)/2
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
        mid = (c+b)/2
        if a[cur_row][mid] == k:
            return cur_row,mid
        if a[cur_row][mid] > k:
            b = mid - 1
        if a[cur_row][mid] < k:
            c = mid + 1
    return False
d=[[1,2],[3,4]]
print bfs_matrix2(d,4)


        
            