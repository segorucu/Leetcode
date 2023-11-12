class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.tab = defaultdict(list)
        for i, edge in enumerate(edges):
            frm, to, cost = edge
            self.tab[frm].append((to,cost))
        

    def addEdge(self, edge: List[int]) -> None:
        frm, to, cost = edge
        self.tab[frm].append((to,cost))
        return None
        

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf for _ in range(self.n)]
        queue = [(0,node1)]
        visited = set()
        while queue:
            d, node = heapq.heappop(queue)
            if d < dist[node]:
                dist[node] = d
            visited.add(node)
            for neigh,cost in self.tab[node]:
                if neigh not in visited:
                    heapq.heappush(queue,(d+cost,neigh))

        if dist[node2] == inf:
            return -1
        return dist[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)