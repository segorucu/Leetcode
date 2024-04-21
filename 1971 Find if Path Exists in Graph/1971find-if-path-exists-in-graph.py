from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        seen = set()

        def dfs(node):
            seen.add(node)
            if destination in seen:
                return True
            ans = False
            for neighbor in hashtable[node]:
                if neighbor not in seen:
                    ans = ans or dfs(neighbor)
            return ans
                


        hashtable = defaultdict(list)
        for i, j in edges:
            hashtable[i].append(j)
            hashtable[j].append(i)

        ans = dfs(source)
        return ans


