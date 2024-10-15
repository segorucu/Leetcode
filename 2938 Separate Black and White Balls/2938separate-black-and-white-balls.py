from heapq import heapify, heappop, heappush
class Solution:
    def minimumSteps(self, s: str) -> int:
        
        l = 0
        n = len(s)
        r = n-1
        s = list(s)
        cost = 0
        while l < r:
            if s[l] == "1":
                while l < r and s[r] == "1":
                    r -= 1
                if l < r:
                    s[l], s[r] = s[r], s[l]
                    cost += r-l
            l += 1
        return cost
