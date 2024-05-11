class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:


        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node,pp,time):
            visited.add(node)
            if node == target:
                if time > t:
                    return 0
                elif time == t:
                    return pp
                else:
                    unvisited = 0
                    for neigh in graph[node]:
                        if neigh not in visited:
                            unvisited += 1
                    if unvisited:
                        return 0
                    return pp
            
            unvisited = 0
            for neigh in graph[node]:
                if neigh not in visited:
                    unvisited += 1

            res = 0
            for neigh in graph[node]:
                if neigh not in visited:
                    res += dfs(neigh,pp/unvisited,time+1)

            return res


        visited = set()
        return dfs(1,1.,0)