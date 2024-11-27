class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        mp = collections.defaultdict(list)
        for i in range(n-1):
            mp[i].append(i+1)
        
        curr = [0]
        def bfs():
            queue = collections.deque()
            queue.append((0,0))
            visited = set()
            visited.add(0)
            while queue:
                node, dist = queue.popleft()
                if node == n-1:
                    return dist
                for neigh in mp[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh,dist+1))

                
        ans = []
        for u,v in queries:
            mp[u].append(v)      
            ans.append(bfs())


        return ans