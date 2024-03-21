class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        ans = [inf]
        
        def backtrack(sm,i):
            # print(sm,i,ans)
            if sm == target:
                ans[0] = sm
                return True
            elif abs(sm-target) < abs(target-ans[0]):
                ans[0] = sm
            elif abs(sm-target) == abs(target-ans[0]):
                ans[0] = min(ans[0],sm)
            elif sm > 2 * target:
                return False
            if i == m:
                return False

            if backtrack(sm,i+1):
                return True
            if backtrack(sm+toppingCosts[i],i+1):
                return True
            if backtrack(sm+2*toppingCosts[i],i+1):
                return True

            return False

        
        n = len(baseCosts)
        m = len(toppingCosts)
        for base in baseCosts:
            if backtrack(base,0):
                return ans[0]
        return ans[0]

        
        