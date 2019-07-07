'''
Created on Jan 4, 2018

@author: qiankunhuang
'''
def totalOccurrence(array, target):
      """
      array: int[]
      target: int
      return: int
      """
      if not array or len(array) == 0:
        return 0
      left = 0
      right = len(array)-1
      index=0
      count=1
      while left+1 < right:
        mid = int((left+right)/2)
        if array[mid]==target:
          index=mid
          break
        if array[mid]>target:
          right = mid
        if array[mid] < target:
          left = mid
      if array[left] == target:
         index =left
      if array[right] == target:
         index = right
      if array[index] == target:
        for i in range(index-1,-1,-1):
          if array[i] == target:
            count+=1
          else:
            break
        for j in range(index+1,len(array),1):
          if array[j] == target:
            count+=1
          else:
            break
      else:
        return 0
      return count

a =  [1,2,3,4] 
b = [2,3,4,5]
c=[3,4,5,6]  
matrix=[]

for i in range(len(a)):
        for j in range(len(b)):
            d = [[t**2+(a[i])**2+(b[j])**2,(a[i],b[j],t)] for t in c]
            matrix.append(d)
print matrix
     
    
            
            
                