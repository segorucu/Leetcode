class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        

        def knn(edges, k):
            graph = defaultdict(set)
            for a,b in edges:
                graph[a].add(b)
                graph[b].add(a)
            n = len(edges)+1
            ans = n * [0]
            for i in range(n):
                queue = deque()
                queue.append((i,0))
                curr = 0
                visited = set()
                visited.add(i)
                while queue:
                    node, level = queue.popleft()
                    curr += 1
                    for nei in graph[node]:
                        if nei not in visited and level < k:
                            visited.add(nei)
                            queue.append((nei,level+1))
                ans[i] = curr
            return ans

        add = 0
        if k > 0:
            add = max(knn(edges2,k-1))
        ans = knn(edges1,k)

        for i in range(len(ans)):
            ans[i] += add

    
        return ans
