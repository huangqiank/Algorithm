#385. Mini Parser#
#Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.
#Each element is either an integer or a list whose elements may also be integers or other lists.
#Example 1:
#Input: s = "324"
#Output: 324
#Explanation: You should return a NestedInteger object which contains a single integer 324.


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))
        stack = []
        negative = -1
        num =0
        for  i in range(len(s)):
            if s[i] == "[":
                stack.append(NestedInteger())
            if s[i] == "-":
                negative = 1
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in[",", "]"]:
                if s[i-1].isdigit():
                    if negative == 1:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num = 0
                negative = -1
                if s[i] == "]" and len(stack) >1:
                    stack[-2].add(stack.pop())
        return stack.pop()
