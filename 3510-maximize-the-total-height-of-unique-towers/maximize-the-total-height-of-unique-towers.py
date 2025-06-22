class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        maximumHeight.sort()
        tot = 0 
        maxacceptable = inf
        while maximumHeight:
            curr = maximumHeight.pop()
            if curr > maxacceptable:
                curr = maxacceptable
            if curr <= 0:
                return -1
            tot += curr
            maxacceptable = curr - 1

        return tot