class Solution:
    def dfs(self, G, S, signalSpeed):

        queue = collections.deque()
        queue.append((S,0,None))
        sidegraph = collections.defaultdict(int)
        visited = set()
        visited.add(S)
        count = 0
        while queue:
            node, cost, side = queue.popleft()
            if side is not None:
                if cost % signalSpeed == 0:
                    sidegraph[side] += 1
            for neigh, step in G[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    if node == S:
                        side = count
                        count += 1
                    queue.append((neigh,cost+step,side))
        return sidegraph

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        
        graph = collections.defaultdict(list)
        n = len(edges)
        ans = (n+1) * [0]
        for a,b,w in edges:
            graph[a].append((b,w))
            graph[b].append((a,w))
            
        for key,val in graph.items():
            if len(val) < 2:
                continue
            else:
                # print(key)
                sidegraph = self.dfs(graph,key,signalSpeed)
                # print(sidegraph)
                sm = 0
                cnt = 0
                for k,v in sidegraph.items():
                    cnt += sm*v
                    sm += v
                ans[key] = cnt
                # print(ans)
        return ans
             
        
        