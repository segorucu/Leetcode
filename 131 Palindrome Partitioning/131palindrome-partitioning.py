from collections import defaultdict
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = defaultdict(set)
        n = len(s)
        def helper(i,j):
            while i >= 0  and j < n and s[i] == s[j]:
                d[i].add(j)
                i -= 1
                j += 1

        for i in range(n):
            helper(i,i)
            helper(i,i+1)

        ans = []
        def dfs(node,curr):
            if node == n:
                ans.append(curr[:])
                return

            for neigh in d[node]:
                curr.append(s[node:neigh+1])
                dfs(neigh+1,curr)
                curr.pop()


        dfs(0,[])


        return ans
        
        