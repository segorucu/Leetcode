class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n= len(grid)
        full = set(range(1,n**2+1))
        ans = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] in full:
                    full.remove(grid[i][j])
                else:
                    ans.append(grid[i][j])
        full = list(full)
        ans.append(full[0])
        return ans
        