from heapq import heapify, heappop, heappush
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        heap = []
        maxval = 0
        ans = 0
        for event in events:
            start, end, value = event
            while heap and heap[0][0] < start:
                _, val = heappop(heap) 
                maxval = max(maxval,val)
            ans = max(ans,maxval+value)
            heappush(heap,(end,value))
        return ans
