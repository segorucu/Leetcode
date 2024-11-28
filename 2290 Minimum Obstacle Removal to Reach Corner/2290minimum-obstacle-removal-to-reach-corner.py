class Solution:
    def dijkstra(self, G, S, n):
#  G is graph containing G[node] = [(neigh,dist)] ...
#  S is start node
#  n is number of nodes
#  it returns the distance from start node to all the nodes
        distance = n * [float("inf")]
        distance[S] = 0
        previous = n * [None]
        heap = []
        heappush(heap,(distance[S],S))
        
        visited = set()
        while heap:
            dist, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for neigh, cost in G[node]:
                if neigh not in visited:
                    tempDistance = distance[node] + cost
                    if tempDistance < distance[neigh]:
                        distance[neigh] = tempDistance
                        previous[neigh] = node
                        heappush(heap,(tempDistance,neigh))
        return distance, previous

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        def convert(r,c):
            return n*r + c

        graph = collections.defaultdict(list)

        for r in range(m):
            for c in range(n):
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if valid(nr,nc):
                        graph[convert(r,c)].append((convert(nr,nc),grid[nr][nc]))
        
        dist, _ = self.dijkstra(graph,0,m*n)
        return dist[-1]