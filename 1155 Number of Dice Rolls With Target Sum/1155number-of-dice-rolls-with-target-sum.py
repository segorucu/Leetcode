from functools import cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def backtrack(it,sm):
            if it == 0:
                if sm == target:
                    return 1
                
            if sm + it*k < target:
                return 0
            res = 0
            for j in range(1,k+1):
                sm += j
                if sm > target:
                    break
                res += backtrack(it-1,sm)
                sm -= j

            return res
            
        if k*n < target:
            return 0
        res = backtrack(n,0)

        return res % (10**9 + 7)