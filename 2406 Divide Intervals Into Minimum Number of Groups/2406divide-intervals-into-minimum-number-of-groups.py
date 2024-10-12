from sortedcontainers import SortedList
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        endlist = SortedList()
        for b,e in intervals:
            i = endlist.bisect_left(b)-1
            if 0 <= i < len(endlist):
                endlist.pop(i)
                endlist.add(e)
            else:
                endlist.add(e)
            
        return len(endlist)