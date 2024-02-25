class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 1:
            return True
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(prev,node):
            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    one = dfs(node,neigh)
                    if not one:
                        return one
                else:
                    if neigh != prev:
                        return False
            return True

        res = dfs(None,0)
        return res and len(visited) == n
        