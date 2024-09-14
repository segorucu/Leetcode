class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        Xsum = [n*[0] for _ in range(m)]
        Ysum = [n*[0] for _ in range(m)]

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "X":
                    Xsum[r][c] += 1
                if grid[r][c] == "Y":
                    Ysum[r][c] += 1
                if c > 0:
                    Xsum[r][c] += Xsum[r][c-1]
                    Ysum[r][c] += Ysum[r][c-1]
                if r > 0:
                    Xsum[r][c] += Xsum[r-1][c]
                    Ysum[r][c] += Ysum[r-1][c]
                if r > 0 and c > 0:
                    Xsum[r][c] -= Xsum[r-1][c-1]
                    Ysum[r][c] -= Ysum[r-1][c-1]
                if Xsum[r][c] == Ysum[r][c] and Xsum[r][c] > 0:
                    ans += 1

        return ans
                

