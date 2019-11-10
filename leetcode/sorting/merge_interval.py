# _*_coding:utf-8_*_
##多维度排序，先按照第一维度排序，再按照第二维度排序
###输入: [[1,3],[2,6],[8,10],[15,18]]
###输出: [[1,6],[8,10],[15,18]]
##新建res
##找中间集合
##有交集和左边合并，再找中间，循环
##没有交集则写入res

def intersect(a, b):
    ## 不相交，
    if a[1] < b[0]:
        return 0
    ## 包含
    if a[1] >= b[1]:
        return -1
    ## 相交
    return 1


def merge(a, b):
    c = [a[0], b[1]]
    return c


def merge_interval(input):
    input = sorted(input, key=lambda k: (k[0], k[1]))
    res = []
    res.append(input[0])
    for i in range(1, len(input), 1):
        last_interval = res[-1]
        if 1 == intersect(last_interval, input[i]):
            res.pop()
            res.append(merge(last_interval, input[i]))
        if 0 == intersect(last_interval, input[i]):
            res.append(input[i])
    return res


input = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_interval(input))
input2 = [[1, 2], [4, 5], [3, 4], [1, 9], [1, 7]]
print(merge_interval(input2))
##多维度排序，先按照第一维度排序，再按照第一维度排序
print(sorted(input2, key=lambda k: (k[0], k[1])))
