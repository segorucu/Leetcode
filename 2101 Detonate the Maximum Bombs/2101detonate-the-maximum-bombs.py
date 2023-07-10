from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def diff(xi,yi,xj,yj):
            ans = ((xi-xj)**2+(yi-yj)**2)**0.5
            return ans

        def dfs(i):
            visited.add(i)
            for neigh in bombdict[i]:
                if neigh not in visited:
                    dfs(neigh)
            return len(visited)

        n = len(bombs)
        if n == 1:
            return 1

        bombdict = defaultdict(list)
        for i in range(n):
            xi,yi,ri = bombs[i]
            for j in range(n):
                xj,yj,rj = bombs[j]
                dist = diff(xi,yi,xj,yj)
                if dist <= ri:
                    bombdict[i].append(j)

        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans,dfs(i))

                

        return ans

