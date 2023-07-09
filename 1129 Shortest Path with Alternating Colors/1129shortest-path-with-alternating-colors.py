from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        reds = defaultdict(list)
        for i,j in redEdges:
            reds[i].append(j)
        blues = defaultdict(list)
        for i,j in blueEdges:
            blues[i].append(j)

        seen = set()
        seen.add((0,'o'))
        values = [float("inf")] * n

        queue = deque()
        queue.append((0,'rb',0))
        while queue:
            loc, color, steps = queue.popleft()
            values[loc] = min(steps,values[loc])
            if "r" in color:
                for neighbor in reds[loc]:
                    if (neighbor,'b') not in seen:
                        seen.add((neighbor,'b'))
                        queue.append((neighbor,'b',steps+1))
            if "b" in color:
                for neighbor in blues[loc]:
                    if (neighbor,'r') not in seen:
                        seen.add((neighbor,'r'))
                        queue.append((neighbor,'r',steps+1))

        for i in range(n):
            if values[i] == float("inf"):
                values[i] = -1

        return values

