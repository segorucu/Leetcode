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

    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:

        G = collections.defaultdict(list)
        for a,b,cost in roads:
            G[a-1].append((b-1,(k+1)*cost))
            G[b-1].append((a-1,(k+1)*cost))

        ans = n * [0]
        for start in range(n):

            distance, previous = self.dijkstra(G, start, n)
            for i in range(n):
                distance[i] += appleCost[i]
            ans[start] = min(distance)

        return ans

        
        
        