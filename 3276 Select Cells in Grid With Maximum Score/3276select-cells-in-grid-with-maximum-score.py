from functools import cache
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        unique = set()
        mp = collections.defaultdict(list)
        for r in range(m):
            for c in range(n):
                unique.add(grid[r][c])
                mp[grid[r][c]].append(r)

        unique = sorted(unique, reverse = True)

        @cache
        def dp(i,mask):
            if i == len(unique):
                return 0

            ans = 0
            for r in mp[unique[i]]:
                if not (mask & (1 << r)):
                    ans = max(ans, unique[i] + dp(i+1,mask | (1 << r)))
            ans = max(ans, dp(i+1, mask))
            return ans

        

        return dp(0,0)
