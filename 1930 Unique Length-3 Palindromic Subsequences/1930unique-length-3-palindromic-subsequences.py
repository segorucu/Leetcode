class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        graph = collections.defaultdict(set)
        visited = set()
        for a in s:
            if a in graph:
                for center in graph[a]:
                    visited.add(a+center+a)
            for pre in graph.keys():
                graph[pre].add(a)
            if a not in graph:
                graph[a] = set()

        # print(visited)
        return len(visited)

