class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        

        query_list = []
        for i,q in enumerate(queries):
            query_list.append((q,i))
        query_list.sort()

        k = len(queries)
        ans = k * [0]
        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        visited = set()
        visited.add((0,0))
        hp = [(grid[0][0],0,0)]
        points = 0

        for limit, index in query_list:
            while hp and hp[0][0] < limit:
                val, r, c = heappop(hp)
                points += 1
                neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr,nc in neighs:
                    if valid(nr,nc) and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        heappush(hp,(grid[nr][nc],nr,nc))
            ans[index] = points
            

        return ans
