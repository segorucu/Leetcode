from collections import defaultdict, deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        group = defaultdict(int)
        queue = deque()

        current = 0

        for i in range(1,n+1):
            queue.append(i)
            while queue:
                node = queue.popleft()
                if node not in group:
                    current = 0 
                    group[node] = current
                else:
                    current = group[node]
                current = 1 - current
                for neigh in adj[node]:
                    if neigh in group:
                        if group[neigh] != current:
                            return False
                    else:
                        group[neigh] = current
                        queue.append(neigh)

        return True
            



        return True
        