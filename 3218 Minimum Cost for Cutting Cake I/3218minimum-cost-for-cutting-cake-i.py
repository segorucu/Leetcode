class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        def recurse(m, n, horizontalCut, verticalCut):
            # print(m, n, horizontalCut, verticalCut)
            if m == 1:
                return sum(verticalCut)
            if n == 1:
                return sum(horizontalCut)

            maxh = max(horizontalCut)
            maxv = max(verticalCut)
            if maxh > maxv:
                ind = horizontalCut.index(maxh)
                cost = recurse(ind+1, n, horizontalCut[0:ind], verticalCut) + maxh
                cost += recurse(m-ind-1, n, horizontalCut[ind+1:], verticalCut)
                return cost
            else:
                ind = verticalCut.index(maxv)
                cost = recurse(m, ind+1, horizontalCut, verticalCut[0:ind]) + maxv
                cost += recurse(m, n-ind-1, horizontalCut, verticalCut[ind+1:])
                return cost

        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        return recurse(m, n, horizontalCut, verticalCut)