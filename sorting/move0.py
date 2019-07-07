class Solution(object):
    def kClosest(self, array, target, k):
        if k==0:
            return []
        res=[]
        t=self.find_closet(array,target)
        i = t  
        j = t+1    
        while k>0:
            if i<0:
                res.extend(array[j:j+k])
                return res
            if j >len(array)-1:
                while k >0:
                    res.append(array[i])
                    i-=1
                    k-=1
                return res
            if abs(target-array[i]) < abs(target-array[j]):
                res.append(array[i])
                i-=1
            else:
                res.append(array[j])
                j+=1
            k-=1
        return res
    def find_closet(self,array,target):
        if not array or len(array) == 0:
            return  -1
        left = 0
        right = len(array)-1
        while left+1 < right:
            mid = (left+right)/2
            if array[mid]==target:
                return mid
            if array[mid] > target :
                right = mid
            if array[mid] < target :
                left = mid
        if abs(array[left]- target)<abs(array[right]- target):
            return left
        else:
            return right
print Solution().kClosest([1,5,7],7,2)
print 3/2
