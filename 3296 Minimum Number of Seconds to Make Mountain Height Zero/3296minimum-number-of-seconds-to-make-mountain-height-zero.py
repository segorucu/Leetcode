from heapq import heapify, heappop, heappush
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def maxHeightReduced(workerTime: int, time: int) -> int:
            # Binary search to find the maximum height worker can reduce within `time` seconds
            left, right = 0, mountainHeight
            while left < right:
                mid = (left + right + 1) // 2
                # Calculate the time it takes to reduce `mid` height units
                # Using sum of arithmetic series: workerTime * (mid * (mid + 1)) // 2
                if workerTime * (mid * (mid + 1)) // 2 <= time:
                    left = mid  # Can reduce this much height, try for more
                else:
                    right = mid - 1  # Cannot reduce this much, try for less
            return left

        # Binary search over the total time
        left, right = 0, 10**18  # Large enough upper bound for time

        while left < right:
            mid = (left + right) // 2
            total_height_reduced = 0

            # Check how much height can be reduced in `mid` seconds
            for wt in workerTimes:
                total_height_reduced += maxHeightReduced(wt, mid)
                if total_height_reduced >= mountainHeight:
                    break

            if total_height_reduced >= mountainHeight:
                right = mid  # Try to find a smaller possible time
            else:
                left = mid + 1  # Increase the time

        return left

        
        heap = []
        for val in workerTimes:
            heappush(heap, (val, val, 1))
        heapify(workerTimes)
        ans = 0
        while mountainHeight > 0:
            totaltime, origcost, count = heappop(heap)
            mountainHeight -= 1
            ans = max(ans, totaltime)
            count += 1
            totaltime = origcost * ((count * (count+1)) // 2)
            heappush(heap, (totaltime, origcost, count))
           

        return ans