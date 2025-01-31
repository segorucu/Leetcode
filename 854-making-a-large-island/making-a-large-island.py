class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])

        groups = collections.defaultdict(set)

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n 

        def dfs(r,c):
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in neighs:
                if valid(nr,nc) and (nr,nc) not in curr and grid[nr][nc] == 1:
                    curr.add((nr,nc))
                    dfs(nr, nc)

        group = 0
        visited = set()
        groupindex = collections.defaultdict(int)
        ans = 1
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == 1:
                    curr = set()
                    curr.add((r,c))
                    dfs(r,c)
                    visited.update(curr)
                    groups[group] = curr
                    ans = max(ans, len(curr)+1)
                    for nr,nc in curr:
                        groupindex[(nr,nc)] = group
                    group += 1

        if len(groups.keys()) == 1:
            return min(m*n,ans)

        for group in groups:
            print(len(groups[group]))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                    tmp = 0
                    visited = set()
                    for nr, nc in neighs:
                        if (nr,nc) not in groupindex:
                            continue
                        group = groupindex[(nr,nc)]
                        if group not in visited:
                            tmp += len(groups[group])
                            visited.add(group)
                    ans = max(ans, tmp + 1)

        return ans


# [0,1,0],
# [1,0,1],
# [1,0,0]]