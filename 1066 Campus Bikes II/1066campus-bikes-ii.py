from functools import cache
class Solution:
    def __init__(self):
        self.ans = float("inf")

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)
        def calcdist(curr):
            sm = 0
            for worker, bike in enumerate(curr):
                sm += abs(workers[worker][0]-bikes[bike][0]) + abs(workers[worker][1]-bikes[bike][1])
            return sm
        
        visited = set()
        # @cache
        def backtrack(wi,bi,sm):
            if wi == n:
                return sm

            res = float("inf")
            for j in range(m):
                if j not in visited:
                    add = abs(workers[wi][0]-bikes[j][0]) + abs(workers[wi][1]-bikes[j][1])
                    if sm+add > res:
                        continue
                    visited.add(j)
                    res = min(res,backtrack(wi+1,j+1,sm+add))
                    visited.remove(j)
            return res

        

        return backtrack(0,0,0)