class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)

        two, one = cost[0], cost[1]
        for i in range(2,n):
            one, two = min(two,one) + cost[i], one
            
        

        return min(one,two)
        