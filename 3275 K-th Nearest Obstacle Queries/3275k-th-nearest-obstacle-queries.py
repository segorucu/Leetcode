from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        darr = SortedList()
        results = []
        for a,b in queries:
            darr.add(abs(a)+abs(b))
            if len(darr) < k:
                results.append(-1)
            else:
                results.append(darr[k-1])
            while len(darr) > k:
                darr.pop()

        return results
