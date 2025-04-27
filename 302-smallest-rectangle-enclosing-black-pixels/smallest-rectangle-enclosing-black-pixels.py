class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        

        m = len(image)
        n = len(image[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and image[r][c] == "1"

        def dfs(r,c):
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc)

        visited = set()
        visited.add((x,y))
        dfs(x,y)

        minrow = inf
        maxrow = 0
        mincol = inf
        maxcol = 0
        for r,c in visited:
            minrow = min(minrow,r)
            maxrow = max(maxrow,r)
            mincol = min(mincol,c)
            maxcol = max(maxcol,c)

    
        return (maxcol-mincol+1)*(maxrow-minrow+1)