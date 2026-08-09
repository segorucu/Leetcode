class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        graph = collections.defaultdict(set)
        for region in regions:
            n = len(region)
            for i in range(1, n):
                graph[region[i]].add(region[0])


        seen = set()
        queue = deque()
        queue.append(region1)
        queue.append(region2)

        while queue:
            node = queue.popleft()
            if node in seen:
                return node
            seen.add(node)
            for neigh in graph[node]:
                queue.append(neigh)

        
