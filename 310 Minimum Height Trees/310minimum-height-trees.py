from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        adj = defaultdict(list)
        indegree = [0] * n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append((i,0))

        maxdepth = -1 
        ans = []      
        while queue:
            node, depth = queue.popleft()
            for neigh in adj[node]:
                indegree[neigh] -= 1
                indegree[node] -= 1
                if indegree[neigh] == 1:
                    queue.append((neigh,depth+1))
            if depth > maxdepth:
                maxdepth = depth
                ans = [node]
            elif depth == maxdepth:
                ans.append(node)

        return ans
                
                


        
         

        return ans


