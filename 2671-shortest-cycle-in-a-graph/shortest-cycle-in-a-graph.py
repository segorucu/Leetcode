from typing import List
import collections
from math import inf

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(start):
            queue = collections.deque([(start, -1, 0)])  # (node, parent, depth)
            seen = {start: 0}  # Stores depth (or distance from start)
            shortest_cycle = inf
            while queue:
                node, parent, depth = queue.popleft()

                for nei in graph[node]:
                    if nei == parent:  
                        continue  # Skip the edge back to the parent

                    if nei in seen:
                        # If already seen and NOT the parent, we found a cycle
                        shortest_cycle = min(shortest_cycle, depth + seen[nei] + 1)  
                        continue

                    seen[nei] = depth + 1
                    queue.append((nei, node, depth + 1))  # Enqueue with updated depth
            
            return shortest_cycle  # No cycle found

        ans = inf
        for i in range(n):
            ans = min(ans, bfs(i))

        return ans if ans != inf else -1
