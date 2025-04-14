class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for p,c in edges:
            graph[p].append(c)
            graph[c].append(p)

        visited = set()
        def dfs(parent):
            ret = 0
            found = False
            if hasApple[parent]:
                found = True
            for child in graph[parent]:
                if child not in visited:
                    visited.add(child)
                    foundchild, depth = dfs(child)
                    ret += depth
                    found = found or foundchild
            if found and parent != 0:
                ret += 1
            # print(parent, found, ret)
            return found, ret

        visited.add(0)
        return 2 * dfs(0)[1]