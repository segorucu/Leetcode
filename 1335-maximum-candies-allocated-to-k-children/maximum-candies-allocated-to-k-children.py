class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def good(val):
            if val == 0:
                return True
            tot = 0
            for candy in candies:
                tot += candy // val
            return tot >= k


        right = sum(candies) // k
        left = 1
        # if right == 0:
        #     return 0
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                left = mid+1
            else:
                right = mid-1

        return res
