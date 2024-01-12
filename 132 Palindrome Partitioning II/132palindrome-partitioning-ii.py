from collections import defaultdict
from functools import cache
class Solution:
    def minCut(self, s: str) -> int:

        d = defaultdict(set)
        n = len(s)

        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                d[i].add(j)
                i -= 1
                j += 1

        for i in range(n):
            helper(i,i)
            helper(i,i+1)

        @cache
        def dfs(node):
            if node == n:
                return 0

            ans = float("inf")
            for neigh in d[node]:
                ans = min(ans,dfs(neigh+1)+1)
            return ans


        return dfs(0)-1
