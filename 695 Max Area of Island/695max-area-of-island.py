class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]  #dx,dy
        seen = set()
        
        def dfs(i,j):
            seen.add((i,j))
            val = 0
            for move in directions:
                if valid(i+move[1],j+move[0]):
                    val += dfs(i+move[1],j+move[0])
            return val + 1

        def valid(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i,j) not in seen:
                return True
            return False

        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in seen:
                    ans = max(ans,dfs(i,j))
                    


        return ans
        
                        