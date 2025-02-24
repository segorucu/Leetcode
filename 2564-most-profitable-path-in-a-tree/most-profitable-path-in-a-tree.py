class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        
        def dfs_bob(node):
            if node == 0:
                return [0]

            path = None
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    path = dfs_bob(nei)
                    if path:
                        path.append(node)
                        return path
            return None

        
        visited = set()
        visited.add(bob)
        path = dfs_bob(bob)
        path.reverse()
        bobs_timeline = collections.defaultdict(int)
        for i,node in enumerate(path):
            bobs_timeline[node] = i

        def dfs_alice(node,time):
            reward = -float("inf")
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    reward = max(reward,dfs_alice(nei,time+1))

            add = 0
            if node in bobs_timeline:
                if time < bobs_timeline[node]:
                    add += amount[node]
                elif time == bobs_timeline[node]:
                    add += amount[node] // 2
            else:
                add += amount[node]

            # print(node,reward,add)
            if reward == -float("inf"):
                return add
            else:
                return reward + add

            



        visited = set()
        visited.add(0)
        return dfs_alice(0,0)
