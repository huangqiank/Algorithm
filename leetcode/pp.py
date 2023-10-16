class Solution:
    def minMutation(self, start, end, bank):
        bank_set = set(bank)
        visited = set()
        tmp = 0
        self.min_count= float("inf")
        self.minMutation_help(start,end,bank_set,visited,tmp)
        if self.min_count == float("inf"):
            return -1
        return self.min_count
    def minMutation_help(self,start,end,bank_set,visited,tmp):
        if start in visited or tmp > 8:
            return
        if start == end:
            self.min_count = min(self.min_count,tmp)
            return
        visited.add(start)
        for i in range(8):
            for char in ["A","C","G","T"]:
                new = start[:i]+ char + start[i+1:]
                if new in bank_set:
                    self.minMutation_help(new,end,bank_set,visited,tmp+1)
        return
s= Solution()
print(s.minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"]))



## （1，10）（2，8） 。。。。（20，30）
## （a,b）
##left = 0 , right = n-1
## mid = int(left+right)/2
## (mid[0]<=a<mid[1])
## count+1
## (a>=mid[1]):
## left = mid
## (a < mid[0]):
##    (mid[0]<b <=mid[1])
##     count+1
##     left =mid
## if count >=3:
## return -1
## add(a,b)
##personal token
##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



