class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        seen = set()

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and land[r][c] == 1 and (r,c) not in seen

        def dfs(r,c):

            if not valid(r,c):
                return -1
            seen.add((r,c))

            right = dfs(r,c+1)
            bottom = dfs(r+1,c)

            return max(bottom,right,r*n+c)

        

        m = len(land)
        n = len(land[0])
        ans = []
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1 and (r,c) not in seen:
                    dum = dfs(r,c)
                    c2 = dum % n
                    r2 = dum // n
                    ans.append([r,c,r2,c2])


        return ans
        