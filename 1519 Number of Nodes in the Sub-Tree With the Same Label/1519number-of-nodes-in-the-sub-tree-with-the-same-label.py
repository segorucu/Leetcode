class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        mp = collections.defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

        visited = set()
        visited.add(0)
        ans = n * [0]
        def dfs(node):

            counter = Counter()
            for neigh in mp[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    counter += dfs(neigh)
                
            if labels[node] in counter:
                counter[labels[node]] += 1
            else:
                counter[labels[node]] = 1
            ans[node] = counter[labels[node]]
            return counter
            

        dfs(0)

        return ans
