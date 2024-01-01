from heapq import heapify, heappop
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(s)
        heapify(g)

        ans = 0
        while g and s:
            greed = heappop(g)
            size = heappop(s)
            while size < greed:
                if not s:
                    return ans
                size = heappop(s) 
            ans += 1
            
        return ans