class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        left = 1
        right = 10**7
        n = len(dist)
        if ceil(hour) < n:
            return -1
        last = dist.pop()



        def calculate(mid):
            time = 0
            for dis in dist:
                time += math.ceil(dis/mid)
            time += last / mid
            return time <= hour

        while left <= right:
            mid = (left + right) // 2
            log = calculate(mid)
            if log:
                right = mid - 1
            else:
                left = mid + 1

        return left
    