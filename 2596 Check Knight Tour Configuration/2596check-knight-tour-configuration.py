class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        

        if grid[0][0] != 0:
            return False

        mp = {} 
        n= len(grid)
        for r in range(n):
            for c in range(n):
                mp[grid[r][c]] = (r,c)

        for i in range(1,n**2):
            prev= mp[i-1]
            curr = mp[i]
            moves = set()
            moves.add(abs(prev[0]-curr[0]))
            moves.add(abs(prev[1]-curr[1]))
            if moves != {1,2}:
                return False

        return True