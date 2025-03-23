class Solution:
    def dijkstra(self, G, S, n):
#  G is graph containing G[node] = [(neigh,dist)] ...
#  S is start node
#  n is number of nodes
#  it returns the distance from start node to all the nodes
        distance = n * [float("inf")]
        dp = n * [0]
        dp[S] = 1
        distance[S] = 0
        heap = []
        heappush(heap,(distance[S],S))
        MOD = 10**9+7
        
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
                        heappush(heap,(tempDistance,neigh))
                        dp[neigh] = dp[node]
                    elif tempDistance == distance[neigh]:
                        dp[neigh] = (dp[neigh] + dp[node]) % MOD
        return distance, dp

    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for a,b,w in roads:
            graph[a].append((b,w))
            graph[b].append((a,w))


        distance, dp = self.dijkstra(graph, 0, n)
        # print(dp)

        

        
        return dp[-1]

        