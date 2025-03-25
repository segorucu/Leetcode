from heapq import heapify, heappush, heappop
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        left = 0
        right = sum(ribbons) // k

        def go(x):
            if x == 0: return True
            count = 0
            for ribbon in ribbons:
                count += (ribbon // x)
            return count >= k

        # mid is the length of the max ribbon
        ret = 0
        while left <= right:
            mid = (left+right) // 2
            if go(mid):
                ret = mid
                left = mid+1  
            else:
                right = mid-1

        return ret

        

        