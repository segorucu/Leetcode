class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def dijkstra(G, S, n,d):
            distance = collections.defaultdict(int)
            for r in range(m):
                for c in range(n):
                    distance[(r,c)] = float("inf")
            distance[S] = 0
            heap = []
            heappush(heap,(distance[S],S))
            
            visited = set()
            while heap:
                dist, node = heappop(heap)
                if node == d:
                    break
                if node in visited:
                    continue
                visited.add(node)
                for neigh, cost in G[node]:
                    if neigh not in visited:
                        tempDistance = distance[node] + cost
                        if tempDistance < distance[neigh]:
                            distance[neigh] = tempDistance
                            heappush(heap,(tempDistance,neigh))
            return distance

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] == 0

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        graph = collections.defaultdict(list)
        m = len(maze)
        n = len(maze[0])
        for r in range(m):
            for c in range(n):
                if maze[r][c] == 1:
                    continue
                for dx, dy in directions:
                    nc = c + dx
                    nr = r + dy
                    while valid(nr,nc):
                        nc = nc + dx
                        nr = nr + dy
                    nc = nc - dx
                    nr = nr - dy 
                    dist = abs(nc-c) + abs(nr-r)
                    if dist != 0:
                        graph[(r,c)].append(((nr,nc),dist))

        start = (start[0],start[1])
        destination = (destination[0],destination[1])
        distance = dijkstra(graph,start,m*n,destination)

        if distance[destination] == float("inf"):
            return -1
        else:
            return distance[destination]
        return 
                

        