class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        n = len(edges)+1
        def explore(node):
            queue = collections.deque()
            queue.append((node,0))
            visited = set()
            visited.add(node)

            while queue:
                node, dist = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh,dist+1))
            return node, dist

        B, dist= explore(0)
        C, dist = explore(B)

        return dist

