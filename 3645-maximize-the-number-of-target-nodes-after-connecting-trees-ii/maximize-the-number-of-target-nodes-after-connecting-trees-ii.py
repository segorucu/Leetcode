class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        def calculate(edges):
            graph = defaultdict(list)
            for a,b in edges:
                graph[a].append(b)
                graph[b].append(a)

            queue = deque()
            queue.append((0,0))

            evens = odds = 0
            visited = set()
            visited.add(0)
            evenset = set()
            while queue:
                node, level = queue.popleft()
                if level % 2 == 0:
                    evens += 1
                    evenset.add(node)
                else:
                    odds += 1
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei,level+1))
            return evens, odds, evenset

        evens, odds, evenset = calculate(edges1)
        n = len(edges1) + 1
        ans = n * [0]
        for i in range(n):
            if i in evenset:
                ans[i] = evens
            else:
                ans[i] = odds

        evens, odds, evenset = calculate(edges2)
        add = max(evens, odds)
        for i in range(n):
            ans[i] += add

        return ans