class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:


        m = len(grid)
        n = len(grid[0])
        directions = [(0,1,"D"),(1,0,"R"),(0,-1,"U"),(-1,0,"L")] #dcol,drow

        def valid(row,col):
            return 0 <= row < m and 0 <= col < n


        visited = set()
        def explore(row,col,to):
            visited.add((row,col))
            curr.append(to)
            for dcol,drow,to in directions:
                nrow = row + drow
                ncol = col + dcol
                if valid(nrow,ncol) and grid[nrow][ncol] == 1 and (nrow,ncol) not in visited:
                    explore(nrow,ncol,to)
            curr.append("0")

        distinct = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in visited:
                    curr = []
                    row_origin = row
                    col_origin = col
                    explore(row,col,"0")
                    curr = tuple(curr)
                    distinct.add(curr)


        return len(distinct)