class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        directions = ([0,1],[1,0],[0,-1],[-1,0])
        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i,j) not in visited

        def falling(i,j):
            return i == 0 or i == m-1 or j == 0 or j == n-1

        
        def dfs(i,j):
            visited.add((i,j))
            new.add((i,j))
            if falling(i,j):
                self.falling = True
            for move in directions:
                newy, newx = i + move[0], j + move[1]
                if valid(newy,newx):
                    dfs(newy,newx)
            return


        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.falling = False
                    new = set()
                    dfs(i,j)
                    new = list(new)
                    if not self.falling:
                        ans += len(new)

        return ans