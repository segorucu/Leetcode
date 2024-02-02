class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        graph = collections.defaultdict(str)
        for a,b in zip(range(1,9),range(2,10)):
            graph[str(a)] = str(b)
        
        ans = []
        for key in graph.keys():
            cand = key
            while int(cand) < low and cand[-1] in graph:
                cand += graph[cand[-1]]
            while low <= int(cand) <= high:
                ans.append(int(cand))
                if cand[-1] not in graph:
                    break
                cand += graph[cand[-1]]
        return sorted(ans)
        