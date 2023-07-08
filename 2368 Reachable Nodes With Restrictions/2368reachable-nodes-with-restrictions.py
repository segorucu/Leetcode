from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node):
            seen.add(node)
            val = 0
            for neighbor in table[node]:
                if neighbor not in seen:
                    val += dfs(neighbor)
            
            return val + 1

        table = defaultdict(list)
        for i, j in edges:
            table[i].append(j)
            table[j].append(i)

        seen = set(restricted)
        return dfs(0)
