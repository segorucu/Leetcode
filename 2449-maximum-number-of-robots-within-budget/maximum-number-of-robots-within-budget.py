class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        l = 0
        n = len(chargeTimes)
        
        queue = SortedList()
        ans = 0
        sm = 0
        for r in range(n):
            queue.add(chargeTimes[r])
            sm += runningCosts[r]
            while queue and (queue[-1] + (r-l+1) * sm) > budget:
                sm -= runningCosts[l]
                queue.remove(chargeTimes[l])
                l += 1
            ans = max(ans, r-l+1)


        return ans