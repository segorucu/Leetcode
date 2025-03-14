class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def good(val):
            if val == 0:
                return True
            tot = 0
            for candy in candies:
                tot += candy // val
            # print(tot, val)
            return tot >= k

        # print(good(5))

        right = sum(candies) // k
        left = 0
        if right == 0:
            return 0

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                left = mid + 1
            else:
                right = mid
        # print(mid)
        if good(mid+1): return mid+1
        if good(mid): return mid
        if good(mid-1): return mid-1
        return mid
