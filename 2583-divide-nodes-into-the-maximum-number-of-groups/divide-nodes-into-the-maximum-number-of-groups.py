class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        

        adj = collections.defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def getconnectedcomps(i):
            q = deque()
            q.append(i)
            arr = set()
            while q:
                node = q.popleft()
                arr.add(node)
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
            return arr

        def getdist(node):

            dist = {node:1}
            q = deque()
            q.append((node,1))
            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue

                    q.append((nei,length+1))
                    dist[nei] = length+1
            return max(dist.values())

                    

        visited = set()
        res = 0
        for i in range(1,n+1):
            if i in visited:
                continue

            visited.add(i)
            arr = getconnectedcomps(i)

            max_cnt = 0 
            for src in arr:
                ret = getdist(src)
                if ret == -1:
                    return -1
                max_cnt = max(max_cnt, ret)
            res += max_cnt

        return res


