class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def helper(tm):
            tot = 0
            for tim in time:
                tot += tm // tim
            return tot >= totalTrips

        left = 1
        right = max(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            