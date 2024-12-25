class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        count = 0
        def dfs(cur, par):
            total = values[cur]
            for nei in adj[cur]:
                if nei != par: 
                    total += dfs(nei,cur)
            if total % k == 0:
                nonlocal count
                count += 1
            return total
                
        dfs(0,-1)
        return count