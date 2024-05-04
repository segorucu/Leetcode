class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        

        def dfs(i,level):
            curr = level
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    curr += dfs(neigh,level+1)
            return curr

        count_children = n * [0]
        def dfs2(i):
            children = 1
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    children += dfs2(neigh)
            count_children[i] = children
            return children
                
            
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        answer = n * [0]
        visited = set()
        visited.add(0)
        answer[0] = dfs(0,0)

        visited = set()
        visited.add(0)
        dfs2(0)

        def dfs3(node):
            for neigh in graph[node]:
                if neigh not in visited:
                    answer[neigh] = answer[node] + n - 2 * count_children[neigh]
                    visited.add(neigh)
                    dfs3(neigh)

        visited = set()
        visited.add(0)
        dfs3(0)

        return answer