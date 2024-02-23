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

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for s,d,c in times:
            graph[s-1].append((d-1,c))

        distance, _ =self.dijkstra(graph,k-1,n)
        ans = max(distance)
        if ans == float("inf"):
            return -1
        return ans
        