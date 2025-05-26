class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)

        n = len(colors)
        colorhash = {}
        for c in colors:
            if c not in colorhash:
                colorhash[c] = len(colorhash)
        m = len(colorhash)

        colormp = [m * [0] for _ in range(n)]

        def dfs(node):
            if node in path:
                return float("inf")

            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorind = colorhash[colors[node]]
            colormp[node][colorind] = 1
            for nei in adj[node]:
                ret = dfs(nei)
                if ret == float("inf"):
                    return ret

                for c, color in colorhash.items():
                    colormp[node][color] =\
                    max(colormp[node][color],
                        colormp[nei][color]
                        + (1 if color == colorind else 0))
            path.remove(node)

            return max(colormp[node])


        res = 0
        visit, path = set(), set()
        for i in range(n):
            res = max(dfs(i), res)
            if res == float("inf"):
                return -1

        return res

