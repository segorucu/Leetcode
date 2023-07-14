from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for req, course in relations:
            indegree[course] += 1
            adj[req].append(course)
            
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append((i,1))
          
        tot = 0
        while queue:
            node, year = queue.popleft()
            tot += 1
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append((neigh,year+1))
                    
        if tot < n:
            return -1
        
        return year
        