from heapq import heapify, heappop, heappush
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        

        hp = []
        for cost, req in tasks:
            heappush(hp,(cost-req,cost,req))

        ans = curr = 0
        while hp:
            _, cost, req = heappop(hp)
            if curr < req:
                add = req - curr
                curr += add
                ans += add
            curr -= cost
        return ans