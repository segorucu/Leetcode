class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        

        n = len(nums)

        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        XORtab = defaultdict(int)
        visited = set()
        timer = defaultdict(list)
        def dfs(node, time):
            timer[node].append(time)
            XORval = nums[node]
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    ret, time = dfs(neigh, time+1)
                    XORval = XORval ^ ret
            timer[node].append(time+1)
            XORtab[node] = XORval
            return XORval, time + 1

        visited.add(0)
        TOTALxor, time = dfs(0,0)

        def isAncestor(a,b):
            return timer[a][0] < timer[b][0] and timer[a][1] > timer[b][1]

        ans = float("inf")
        for i in range(n-1):
            a, b = edges[i]
            if isAncestor(a,b):
                a, b = b, a
            for j in range(i+1,n-1):
                c, d = edges[j]
                if isAncestor(c,d):
                    c, d = d, c
                if isAncestor(a,c):
                    X1 = TOTALxor ^ XORtab[a]
                    X2 = XORtab[a] ^ XORtab[c]
                    X3 = XORtab[c]
                elif isAncestor(c,a):
                    X1 = TOTALxor ^ XORtab[c]
                    X2 = XORtab[a] ^ XORtab[c]
                    X3 = XORtab[a]
                else:
                    X1 = TOTALxor ^ XORtab[a] ^ XORtab[c]
                    X2 = XORtab[a]
                    X3 = XORtab[c]
                ans = min(ans, max(X1, X2, X3) - min(X1, X2, X3))
            
        return ans
                

