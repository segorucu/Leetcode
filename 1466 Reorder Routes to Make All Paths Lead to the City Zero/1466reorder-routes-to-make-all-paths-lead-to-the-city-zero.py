from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        self.ans = 0
        def dfs(node):
            seen.add(node)
            for neighbor in undirected[node]:
                if neighbor not in seen:
                    if (node,neighbor) in roads:
                        self.ans += 1
                    seen.add(neighbor)
                    dfs(neighbor)
                    

        seen = set()
        roads = set()
        undirected = defaultdict(list)
        for i, j in connections:
            undirected[i].append(j)
            undirected[j].append(i)
            roads.add((i,j))

        dfs(0)
        return self.ans

                    





        return ans