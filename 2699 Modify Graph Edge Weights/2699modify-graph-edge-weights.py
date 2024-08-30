from copy import deepcopy
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

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        G = collections.defaultdict(list)
        for a,b,dist in edges:
            if dist > 0:
                G[a].append((b,dist))
                G[b].append((a,dist))

        MAXVAL = 10**9
        dist, prev = self.dijkstra(G, source, n)
        if dist[destination] < target:
            return []
        elif dist[destination] == target:
            r = 0
            while r < len(edges):
                if edges[r][2] == -1:
                    edges[r] = (edges[r][0], edges[r][1], MAXVAL)
                r += 1
            return edges


        
        G2 = deepcopy(G)
        for a,b,dist in edges:
            if dist == -1:
                G2[a].append((b,1))
                G2[b].append((a,1))

        
        dist, prev = self.dijkstra(G2, source, n)
        
        if dist[destination] > target:
            return []

        r = 0 
        total = inf
        
        while r < len(edges) and total > target:
            while r < len(edges) and edges[r][2] > 0:
                r += 1
            if r >= len(edges):
                return []
            a,b,d = edges[r]
            G[a].append((b,1))
            G[b].append((a,1))  
            edges[r] = (a,b,1)   
            dist, prev = self.dijkstra(G, source, n)
            if dist[destination] <= target:
                edges[r] = (a,b,target-dist[destination]+1)
                while r < len(edges) -1:
                    r += 1
                    if edges[r][2] == -1:
                        edges[r] = (edges[r][0], edges[r][1], MAXVAL)
                return edges


        return []