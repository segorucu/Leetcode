class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:


        n = len(grid)
        cstgr = [[0 for _ in range(n)] for _ in range(n)]
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def valid(i,j):
            return 0 <= i < n and 0 <= j < n and (i,j) not in visited

        stack = []
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i,j,0))
                    visited.add((i,j))
                 
        curr = []
        costset = set()
        while stack:
            i,j,cost = stack.pop()
            cstgr[i][j] = cost
            costset.add(cost)
            for dx,dy in directions:
                ni = i + dy
                nj = j + dx
                if valid(ni,nj):
                    visited.add((ni,nj))
                    curr.append((ni,nj,cost+1))
            if not stack:
                stack = curr
                curr = []

        costlist = list(costset)
        costlist.sort()

        def dfs(i,j,minval):
            if cstgr[i][j] < minval:
                return False
            if i == j == n-1:
                return True

            res = False
            for dx,dy in directions:
                ni = i + dy
                nj = j + dx
                if valid(ni,nj) and cstgr[ni][nj] >= minval:
                    visited.add((ni,nj))
                    res |= dfs(ni,nj,minval)
            return res

        l = 0
        r = len(costlist)-1
        while l <= r:
            mid = (l+r) // 2
            visited = set()
            visited.add((0,0))
            res =  dfs(0,0,costlist[mid])
            # print(l,r,mid,costlist,res)
            if res:
                l = mid + 1
            else:
                r = mid - 1

        return costlist[r]






        return 0
        