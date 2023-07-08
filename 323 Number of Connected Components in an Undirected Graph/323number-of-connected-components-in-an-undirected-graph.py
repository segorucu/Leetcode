from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        seen = set()
        def dfs(node):
            seen.add(node)
            for neighbor in table[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        table = defaultdict(list)
        for i,j in edges:
            table[i].append(j)
            table[j].append(i)

        group = 0
        for i in range(n):
            if i not in seen:
                group += 1
                dfs(i)

        return group