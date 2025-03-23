class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        


        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i):
            for j in graph[i]:
                if j in visited:
                    continue
                visited.add(j)
                curr.add(j)
                dfs(j)


        visited = set()
        component = 0
        for i in range(n):
            if i in visited:
                continue

            visited.add(i)
            curr = set()
            curr.add(i)
            dfs(i)
            n = len(curr)
            for k in curr:
                if len(graph[k]) != n-1:
                    break
            else:
                component += 1

        return component