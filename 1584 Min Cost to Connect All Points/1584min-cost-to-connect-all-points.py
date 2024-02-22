class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

        # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

        #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        return result
class Solution:
    # Kruskal's algorithm in Python

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calcdist(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        n = len(points)
        g = Graph(n)
        for i in range(n):
            x = points[i]
            for j in range(i+1,n):
                y = points[j]
                dist = calcdist(x,y)
                g.add_edge(i,j,dist)
        result = g.kruskal_algo()
        sm = 0
        for a,b,c in result:
            sm += c
        return sm
                
        