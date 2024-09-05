class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = [0]
        visited = set()
        visited.add(0)
        def dfs(node):
            # print(node)
            children = 1
            prev = -1
            good = True
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    curr = dfs(child)
                    children += curr
                    if prev > -1 and prev != curr:
                        good = False
                    prev = curr
            if good:
                ans[0] += 1
            return children

        dfs(0)
        return ans[0]