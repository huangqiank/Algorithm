'''
Created on Jan 4, 2018

@author: qiankunhuang
'''
```

class Solution(object):
    def quickSort(self, array):
        if not array or len(array) <= 1:
            return array
        left = 0
        right = len(array) - 1
        self.help1(array, left, right)
        return array

    def help1(self, array, left, right):
        if left >= right:
            return array
        position = self.help3(array, left, right)
        self.help1(array, position + 1, right)
        self.help1(array, left, position - 1)

    def help3(self, a, left, right):
        l_partition = left - 1
        r_partition = left
        while r_partition < right:
            if a[r_partition] < a[right]:
                l_partition += 1
                a[l_partition], a[r_partition] = a[r_partition], a[l_partition]
                r_partition += 1
            else:
                r_partition += 1
        l_partition += 1
        a[l_partition], a[right] = a[right], a[l_partition]
        return l_partition
