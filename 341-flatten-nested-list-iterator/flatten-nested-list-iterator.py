# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def recurse(self, arr):
        ans = []
        for curr in arr:
            if curr._integer is not None:
                ans.append(curr._integer)
            else:
                ans.extend(self.recurse(curr._list))
        return ans

    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []
        for curr in nestedList:
            if curr._integer is not None:
                self.lst.append(curr._integer)
            else:
                self.lst.extend(self.recurse(curr._list))

        self.n = len(self.lst)
        self.i = 0
        
    
    def next(self) -> int:
        ret = self.lst[self.i]
        self.i += 1
        return ret
        
    
    def hasNext(self) -> bool:
        return self.i < self.n
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())