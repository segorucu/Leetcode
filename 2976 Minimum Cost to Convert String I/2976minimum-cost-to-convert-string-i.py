from collections import deque, defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
            
        nV = 26
        dist = [nV*[float("inf")] for _ in range(nV)]
        for i in range(nV):
            dist[i][i] = 0
            
        def ordinance(a):
            return ord(a) - ord('a')            
        
        for s, t, c in zip(original,changed,cost):
            dist[ordinance(s)][ordinance(t)] = min(dist[ordinance(s)][ordinance(t)],c)
                
        for k in range(nV):
                for i in range(nV):
                    for j in range(nV):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
        total = 0
        for s,t in zip(source,target):
            if dist[ordinance(s)][ordinance(t)] == float('inf'):
                return -1
            else:
                total += dist[ordinance(s)][ordinance(t)]
        

        return total