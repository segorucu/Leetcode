class Solution:
    def dijkstra(self, G, S, n):
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

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        mp = collections.defaultdict(list)
        m = len(edges)
        for i in range(m):
            a, b = edges[i]
            p = succProb[i]
            if p == 0.0:
                p = inf
            else:
                p = -math.log2(p)
            # print(p,"p")
            mp[a].append((b,p))
            mp[b].append((a,p))

        # print(mp)
        distance, previous = self.dijkstra(mp, start_node, n)
        # print(distance, previous)
        p = distance[end_node]
        # print(p)
        return 2**(-p)