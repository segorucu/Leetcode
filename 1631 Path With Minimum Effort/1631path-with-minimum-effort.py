class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        nrows = len(heights)
        ncols = len(heights[0])
        

        directions = [(0,-1),(1,0),(0,1),(-1,0)]

        def valid(i,j):
            return 0 <= i < nrows and 0 <= j < ncols and (i,j) not in self.visited

        def bfs(goal):
            queue = [(0,0)]
            self.visited = set()
            self.visited.add((0,0))
            while queue:
                i, j = queue.pop()
                if i == nrows - 1 and j == ncols - 1:
                    return True
                curr = heights[i][j]
                for move in directions:
                    ni, nj = i + move[1], j + move[0]
                    if valid(ni,nj):
                        neigh = heights[ni][nj]
                        eff = abs(neigh-curr)
                        if eff <= goal:
                            queue.append((ni,nj))
                            self.visited.add((ni,nj))
            return False
            
        

        left = 0
        right = max(max(heights)) - min(min(heights))
        while left <= right:
            mid = (left+right) // 2
            if bfs(mid):
                right = mid - 1
            else:
                left = mid + 1


        return left