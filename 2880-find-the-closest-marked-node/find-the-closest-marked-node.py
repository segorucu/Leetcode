class Solution:
    def dijkstra(self, n, s, graph):
        distance = n * [float("inf")]
        distance[s] = 0
        heap = [(s,0)]
        visited = set()
        while heap:
            # print(heap)
            node, dist = heappop(heap)
            visited.add(node)
            for neigh, weight in graph[node]:
                # if neigh in visited:
                #     continue
                temp_distance = dist + weight
                if temp_distance < distance[neigh]:
                    distance[neigh] = temp_distance
                    heappush(heap,(neigh,temp_distance))

        return distance

    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))

        # print(graph)
        distance = self.dijkstra(n, s, graph)


        ans = float("inf")
        for i in marked:
            ans = min(ans, distance[i])

        # print(distance)
        
        return -1 if ans == inf else ans
        